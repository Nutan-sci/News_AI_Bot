import { useState } from 'react'
import { register } from '../src/services/auth'
import { useRouter } from 'next/router'

export default function Register() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const router = useRouter()

  async function submit(e) {
    e.preventDefault()
    try {
      await register(username, email, password)
      router.push('/login')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <main className="p-6">
      <h1 className="text-2xl mb-4">Register</h1>
      <form onSubmit={submit} className="space-y-3 max-w-md">
        <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="username" className="w-full p-2 border" />
        <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="email" className="w-full p-2 border" />
        <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="password" className="w-full p-2 border" />
        <button className="px-4 py-2 bg-green-600 text-white">Register</button>
        {error && <div className="text-red-600">{error}</div>}
      </form>
    </main>
  )
}
