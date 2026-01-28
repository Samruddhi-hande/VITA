import React, { useEffect } from 'react'
import moment from 'moment'
import Markdown from 'react-markdown'
import Prism from 'prismjs'
import { assets } from '../assets/assets'

const Message = ({ message }) => {

  useEffect(() => {
    if (!message.isImage && !message.isVideo) {
      Prism.highlightAll()
    }
  }, [message.content])

  return (

    
    <div className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'} mb-4 gap-2`}>
      
      <div
        className={`max-w-xs md:max-w-md lg:max-w-lg xl:max-w-xl rounded-lg px-3 py-2 ${message.role === 'user'
            ? 'bg-gradient-to-r from-[#A456F7] to-[#3D81F6] text-white'
            : 'bg-gray-100 dark:bg-purple-900/30 text-gray-800 dark:text-white'
          }`}
      >
        {/* Image */}
        {message.isImage && (
          <img
            src={message.content}
            alt=""
            className="rounded-lg w-full"
          />
        )}

        {/* Video */}
        {message.isVideo && (
          <video
            src={message.content}
            controls
            className="rounded-lg w-full"
          />
        )}

        {/* Text / Markdown */}
        {!message.isImage && !message.isVideo && (
          <div className="prose dark:prose-invert max-w-none text-sm reset-tw">
            <Markdown>{message.content}</Markdown>
          </div>
        )}

        {/* Timestamp */}
        <span className="block text-[10px] mt-1 opacity-70 text-right">
          {moment(message.timestamp).fromNow()}
        </span>
      </div>

      {/* User avatar */}
      {message.role === 'user' && (
        <img
          src={assets.user_icon}
          alt=""
          className="w-8 h-8 rounded-full mt-1"
        />
      )}
    </div>
  )
}

export default Message



  //   return (
  //     <div>
  //       {message.role === "user" ? (
  //         <div className='flex items-start justify-end my-4 gap-2'>
  //           <div className='flex flex-col gap-2 p-2 px-4 bg-slate-50 dark:bg-[#57317C]/30 border border-[#80609F]/30 rounded-md max-w-2xl'>
  //             <p className='text-sm dark:text-primary'>{message.content}</p>
  //             <span className='text-xs text-gray-400 dark:text-[#B1A6C0]'>{ moment(message.timestamp).fromNow()}</span>
  //           </div>
  //           <img src={assets.user_icon} alt="" className='w-8 rounded-full' />
  //         </div>
  //       )
  //         :
  //         (
  //           <div className='inline-flex flex-col gap-2 p-2 px-4 max-w-2xl bg-primary/20 dark:bg-[#57317C]/30 border border-[#80609F]/30 rounded-md my-4'>
  //             {message.isImage ? (
  //               <img src={message.content} alt="" className='w-full max-w-md mt-2 rounded-md'/>
  //             ) :
  //               (
  //                 <div className='text-sm dark:text-primary reset-tw'>
  //                   <Markdown>{message.content}</Markdown>
  //                 </div>
  //               )}
  //             <span className='text-xs text-gray-400 dark:text-[#B1A6C0]'>{ moment(message.timestamp).fromNow()}</span>
  //           </div>
  //         )
  //     }
  //     </div>
  //   )
  // }

