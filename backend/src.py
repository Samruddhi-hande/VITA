

# import json
# from typing import List, Optional
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_community.embeddings import HuggingFaceEmbeddings


# class VITAScriptGenerator:
#     def __init__(self, openai_api_key: str, kb_json_path: str, use_web: bool = False, web_urls: Optional[List[str]] = None):
#         self.openai_api_key = openai_api_key
#         self.kb_json_path = kb_json_path
#         self.use_web = use_web
#         self.web_urls = web_urls or []
#         self.base_url = "https://openrouter.ai/api/v1"

#         #  Use local HuggingFace embeddings (no API call)
#         self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#         #  Chat model through OpenRouter
#         self.llm = ChatOpenAI(
#             model="gpt-4o-mini",
#             temperature=0.7,
#             api_key=self.openai_api_key,
#             base_url=self.base_url,
#             default_headers={
#                 "HTTP-Referer": "http://localhost",
#                 "X-Title": "VITA Script Generator"
#             }
#         )

#         # Build knowledge vector store
#         self.vector_store = self._build_vector_store()

#         # Prompt
#         self.chat_prompt = ChatPromptTemplate.from_template("""
# You are a science explainer for beginners.
# Given the following knowledge from the KB:
# {kb_text}

# Generate a clear, engaging script for a short educational video. 
# Include formulas, explanations, and visualization hints.
# """)


#     def _load_json_kb(self) -> List[str]:
#         with open(self.kb_json_path, "r", encoding="utf-8") as f:
#             kb_data = json.load(f)
#         kb_texts = []
#         for entry in kb_data:
#             kb_texts.append(
#                 f"Topic: {entry.get('topic','')}\n"
#                 f"Formula: {entry.get('formula','')}\n"
#                 f"Explanation: {entry.get('explanation','')}\n"
#                 f"Visualization: {entry.get('visualization_hint','')}\n"
#                 f"Related Topics: {', '.join(entry.get('related_topics',[]))}\n"
#                 f"Difficulty: {entry.get('difficulty','')}"
#             )
#         return kb_texts


#     def _load_web_docs(self, urls: List[str]) -> List[str]:
#         all_texts = []
#         for url in urls:
#             try:
#                 loader = WebBaseLoader(url)
#                 docs = loader.load()
#                 all_texts.extend([doc.page_content for doc in docs])
#             except Exception as e:
#                 print(f"⚠️ Error loading {url}: {e}")
#         return all_texts


#     def _build_vector_store(self) -> FAISS:
#         kb_texts = self._load_json_kb()
#         if self.use_web and self.web_urls:
#             web_texts = self._load_web_docs(self.web_urls)
#             kb_texts.extend(web_texts)
#         return FAISS.from_texts(kb_texts, self.embeddings)


#     def query_kb(self, query: str, top_k: int = 2) -> List[str]:
#         docs = self.vector_store.similarity_search(query, k=top_k)
#         return [d.page_content for d in docs]


#     def generate_script(self, topic_query: str) -> str:
#         relevant_docs = self.query_kb(topic_query)
#         kb_text = "\n\n".join(relevant_docs)
#         prompt = self.chat_prompt.format(kb_text=kb_text)
#         response = self.llm.invoke(prompt)
#         return response.content


# # -------------------- Example Usage --------------------
# if __name__ == "__main__":
#     OPENAI_API_KEY = "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"
#     KB_JSON_PATH = "kb.json"

#     topic_query = input("🔍 Enter a topic to generate script for: ")
#     use_web_input = input("🌐 Do you want to include web data? (y/n): ").strip().lower()
#     use_web = use_web_input == "y"
#     web_urls = []

#     if use_web:
#         while True:
#             url = input("Enter a URL to include (or press Enter to stop): ").strip()
#             if not url:
#                 break
#             web_urls.append(url)

#     vita_generator = VITAScriptGenerator(
#         openai_api_key=OPENAI_API_KEY,
#         kb_json_path=KB_JSON_PATH,
#         use_web=use_web,
#         web_urls=web_urls
#     )

#     print("\n⚙️ Generating script, please wait...\n")
#     script = vita_generator.generate_script(topic_query)
#     print("🎬 Generated Script:\n")
#     print(script)
