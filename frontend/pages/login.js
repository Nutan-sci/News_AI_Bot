import { useState } from 'react'
import { login } from '../src/services/auth'
import { useRouter } from 'next/router'

export default function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const router = useRouter()

  async function submit(e) {
    e.preventDefault()
    try {
      await login(username, password)
      router.push('/')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <main className="p-6">
      <h1 className="text-2xl mb-4">Login</h1>
      <form onSubmit={submit} className="space-y-3 max-w-md">
        <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="username" className="w-full p-2 border" />
        <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="password" className="w-full p-2 border" />
        <button className="px-4 py-2 bg-blue-600 text-white">Login</button>
        {error && <div className="text-red-600">{error}</div>}
      </form>
    </main>
  )
}
