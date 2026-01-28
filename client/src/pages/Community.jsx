import React, { useState, useEffect } from 'react'
import { dummyPublishedImages, dummyPublishedVideos } from '../assets/assets' // Add dummyPublishedVideos
import Loading from './Loading'

const Community = () => {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState('all') // 'all', 'image', 'video'

  const fetchItems = async () => {
    // Combine images and videos
    const allItems = [
      ...dummyPublishedImages.map(img => ({ ...img, type: 'image' })),
      ...dummyPublishedVideos.map(vid => ({ ...vid, type: 'video' })) // Uncomment this line
    ]
    setItems(allItems)
    setLoading(false)
  }

  useEffect(() => {
    fetchItems()
  }, [])

  const filteredItems = items.filter(item => {
    if (filter === 'all') return true
    return item.type === filter
  })

  if (loading) return <Loading />

  return (
    <div className='p-6 pt-12 xl:px-12 2xl:px-20 w-full mx-auto h-full overflow-y-scroll'>
      <div className='mb-6 flex items-center justify-between flex-wrap gap-4'>
        <h2 className='text-xl font-semibold text-gray-800 dark:text-purple-100'>
          Community Gallery
        </h2>
        
        {/* Filter Buttons */}
        <div className='flex gap-2'>
          <button
            onClick={() => setFilter('all')}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              filter === 'all'
                ? 'bg-gradient-to-r from-[#A456F7] to-[#3D81F6] text-white'
                : 'bg-gray-200 dark:bg-purple-900/30 text-gray-700 dark:text-purple-200 hover:bg-gray-300 dark:hover:bg-purple-900/50'
            }`}
          >
            All
          </button>
          <button
            onClick={() => setFilter('image')}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              filter === 'image'
                ? 'bg-gradient-to-r from-[#A456F7] to-[#3D81F6] text-white'
                : 'bg-gray-200 dark:bg-purple-900/30 text-gray-700 dark:text-purple-200 hover:bg-gray-300 dark:hover:bg-purple-900/50'
            }`}
          >
            Images
          </button>
          <button
            onClick={() => setFilter('video')}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              filter === 'video'
                ? 'bg-gradient-to-r from-[#A456F7] to-[#3D81F6] text-white'
                : 'bg-gray-200 dark:bg-purple-900/30 text-gray-700 dark:text-purple-200 hover:bg-gray-300 dark:hover:bg-purple-900/50'
            }`}
          >
            Videos
          </button>
        </div>
      </div>

      {filteredItems.length > 0 ? (
        <div className='flex flex-wrap max-sm:justify-center gap-5'>
          {filteredItems.map((item, index) => (
            <div
              key={index}
              className='relative group block rounded-lg overflow-hidden border border-gray-200 dark:border-purple-700 shadow-sm hover:shadow-md transition-shadow duration-300'
            >
              {item.type === 'image' ? (
                <a href={item.imageUrl} target='_blank' rel='noopener noreferrer'>
                  <img
                    src={item.imageUrl}
                    alt=""
                    className='w-full h-40 md:h-50 2xl:h-62 object-cover group-hover:scale-105 transition-transform duration-300 ease-in-out'
                  />
                </a>
              ) : (
                <div className='relative'>
                  <video
                    src={item.videoUrl}
                    className='w-full h-40 md:h-50 2xl:h-62 object-cover'
                    controls
                    preload='metadata'
                  />
                  <div className='absolute top-2 left-2 bg-black/60 backdrop-blur text-white px-2 py-1 rounded text-xs font-medium'>
                    VIDEO
                  </div>
                </div>
              )}
              
              <p className='absolute bottom-0 right-0 text-xs bg-black/50 backdrop-blur text-white px-4 py-1 rounded-tl-xl opacity-0 group-hover:opacity-100 transition duration-300'>
                Created by {item.userName}
              </p>
            </div>
          ))}
        </div>
      ) : (
        <p className='text-center text-gray-600 dark:text-purple-200 mt-10'>
          No {filter === 'all' ? 'content' : filter === 'image' ? 'images' : 'videos'} available.
        </p>
      )}
    </div>
  )
}

export default Community