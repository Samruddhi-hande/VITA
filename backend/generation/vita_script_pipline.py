# vita_script_pipeline.py

import json
from langchain import OpenAI

from langchain.prompts import ChatPromptTemplate

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import WebBaseLoader

from typing import List, Optional

class VITAScriptGenerator:
    def __init__(self, openai_api_key: str, kb_json_path: str, use_web: bool = False):
        self.openai_api_key = openai_api_key
        self.kb_json_path = kb_json_path
        self.use_web = use_web

        # Initialize embeddings and LLM
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=self.openai_api_key)
        self.llm = ChatOpenAI(model_name="phi-3-mini", temperature=0.7, openai_api_key=self.openai_api_key)
        
        # Load KB and create vector store
        self.vector_store = self._build_vector_store()

        # Prompt template
        self.chat_prompt = ChatPromptTemplate.from_template("""
You are a science explainer for beginners.
Given the following knowledge from the KB:
{kb_text}

Generate a clear, engaging script for a short educational video. 
Include formulas, explanations, and visualization hints.
""")

    def _load_json_kb(self) -> List[str]:
        with open(self.kb_json_path, "r", encoding="utf-8") as f:
            kb_data = json.load(f)
        kb_texts = []
        for entry in kb_data:
            kb_texts.append(
                f"Topic: {entry.get('topic','')}\n"
                f"Formula: {entry.get('formula','')}\n"
                f"Explanation: {entry.get('explanation','')}\n"
                f"Visualization: {entry.get('visualization_hint','')}\n"
                f"Related Topics: {', '.join(entry.get('related_topics',[]))}\n"
                f"Difficulty: {entry.get('difficulty','')}"
            )
        return kb_texts

    def _load_web_docs(self, urls: List[str]) -> List[str]:
        all_texts = []
        for url in urls:
            loader = WebBaseLoader(url)
            docs = loader.load()
            all_texts.extend([doc.page_content for doc in docs])
        return all_texts

    def _build_vector_store(self) -> FAISS:
        kb_texts = self._load_json_kb()
        if self.use_web:
            # Example: You can add any URLs you want here
            web_texts = self._load_web_docs(["https://en.wikipedia.org/wiki/Newton's_laws_of_motion"])
            kb_texts.extend(web_texts)
        return FAISS.from_texts(kb_texts, self.embeddings)

    def query_kb(self, query: str, top_k: int = 2) -> List[str]:
        docs = self.vector_store.similarity_search(query, k=top_k)
        return [d.page_content for d in docs]

    def generate_script(self, topic_query: str) -> str:
        relevant_docs = self.query_kb(topic_query)
        kb_text = "\n\n".join(relevant_docs)
        prompt = self.chat_prompt.format(kb_text=kb_text)
        response = self.llm(prompt)
        return response.content

# -------------------- Example Usage --------------------
# if __name__ == "__main__":
#     OPENAI_API_KEY = "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"
#     KB_JSON_PATH = "kb.json"

#     vita_generator = VITAScriptGenerator(
#         openai_api_key=OPENAI_API_KEY,
#         kb_json_path=KB_JSON_PATH,
#         use_web=True  # Set True if you want hybrid KB with web docs
#     )

#     script = vita_generator.generate_script("Explain Newton's First Law for beginners")
#     print(script)

from langchain.llms import OpenAI

llm = OpenAI(model_name="phi-3-mini", temperature=0.7, openai_api_key="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")
print(llm("Explain Newton's First Law in one sentence"))
