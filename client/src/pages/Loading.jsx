import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

const Loading = () => {
  const navigate = useNavigate()

  useEffect(() => { 
    const timeout = setTimeout(() => {
      navigate('/')
    }, 3000)
    return () => clearTimeout(timeout)
  }, [navigate])
  
  return (
    <div className='relative bg-gradient-to-b from-[#242124] to-[#000000] flex flex-col items-center justify-center h-screen w-screen text-white overflow-hidden'>
      
      {/* Animated background circles */}
      <div className='absolute inset-0 overflow-hidden'>
        <div className='absolute top-1/4 left-1/4 w-96 h-96 bg-[#A456F7]/10 rounded-full blur-3xl animate-pulse'></div>
        <div className='absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#3D81F6]/10 rounded-full blur-3xl animate-pulse' style={{ animationDelay: '1s' }}></div>
      </div>

      {/* Main content */}
      <div className='relative z-10 flex flex-col items-center gap-8'>
        
        {/* Logo or Brand Name */}
        <div className='text-center mb-4'>
          <h1 className='text-5xl font-bold bg-gradient-to-r from-[#A456F7] to-[#3D81F6] bg-clip-text text-transparent'>
            QuickGPT
          </h1>
          <p className='text-sm text-purple-300 mt-2'>Intelligent AI Assistant</p>
        </div>

        {/* Spinning circles loader */}
        <div className='relative w-24 h-24'>
          {/* Outer ring */}
          <div className='absolute inset-0 rounded-full border-4 border-transparent border-t-[#A456F7] border-r-[#3D81F6] animate-spin'></div>
          
          {/* Middle ring */}
          <div className='absolute inset-2 rounded-full border-4 border-transparent border-b-[#A456F7] border-l-[#3D81F6] animate-spin' style={{ animationDirection: 'reverse', animationDuration: '1.5s' }}></div>
          
          {/* Inner dot */}
          <div className='absolute inset-0 flex items-center justify-center'>
            <div className='w-4 h-4 bg-gradient-to-r from-[#A456F7] to-[#3D81F6] rounded-full animate-pulse'></div>
          </div>
        </div>

        {/* Loading text with dots animation */}
        <div className='flex items-center gap-2 text-purple-200'>
          <span className='text-lg'>Loading</span>
          <div className='flex gap-1'>
            <span className='w-2 h-2 bg-[#A456F7] rounded-full animate-bounce'></span>
            <span className='w-2 h-2 bg-[#A456F7] rounded-full animate-bounce' style={{ animationDelay: '0.2s' }}></span>
            <span className='w-2 h-2 bg-[#A456F7] rounded-full animate-bounce' style={{ animationDelay: '0.4s' }}></span>
          </div>
        </div>

        {/* Progress bar */}
        <div className='w-64 h-1 bg-purple-900/30 rounded-full overflow-hidden'>
          <div className='h-full bg-gradient-to-r from-[#A456F7] to-[#3D81F6] rounded-full animate-progress'></div>
        </div>

        {/* Subtitle */}
        <p className='text-sm text-purple-300/70 text-center max-w-xs'>
          Preparing your AI experience...
        </p>
      </div>

      {/* Custom CSS for progress animation */}
      <style>{`
        @keyframes progress {
          0% {
            width: 0%;
          }
          100% {
            width: 100%;
          }
        }
        .animate-progress {
          animation: progress 3s ease-in-out forwards;
        }
      `}</style>
    </div>
  )
}

export default Loading