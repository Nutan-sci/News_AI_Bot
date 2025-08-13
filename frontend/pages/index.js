import Head from 'next/head'
import NewsFeed from '../src/components/NewsFeed'

export default function Home() {
  return (
    <div>
      <Head><title>Realtime News</title></Head>
      <main className="p-6">
        <h1 className="text-2xl font-bold mb-4">Realtime News — Demo</h1>
        <NewsFeed category="tech" />
      </main>
    </div>
  )
}
