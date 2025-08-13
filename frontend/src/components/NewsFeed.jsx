import useSWR from 'swr'
import React from 'react'

import { getAuthHeaders } from '../services/auth';
const fetcher = (url) => fetch(process.env.NEXT_PUBLIC_API_URL + url, { headers: {...getAuthHeaders()} }).then(r => r.json())

export default function NewsFeed({ category='tech' }) {
  const { data, error } = useSWR(`/api/articles?category=${category}`, fetcher, { refreshInterval: 5000 })

  if (error) return <div>Error loading feed</div>
  if (!data) return <div>Loading...</div>

  return (
    <div className="space-y-4">
      {data.results.map(a => (
        <article key={a.id} className="p-4 border rounded">
          <a href={a.url} target="_blank" rel="noreferrer" className="text-lg font-semibold">{a.title}</a>
          <p className="text-sm text-gray-600">{a.summary || a.excerpt}</p>
          <div className="text-xs text-gray-500">{a.source} — {new Date(a.published_at).toLocaleString()}</div>
        </article>
      ))}
    </div>
  )
}
