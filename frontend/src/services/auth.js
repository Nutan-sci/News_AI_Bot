export async function login(username, password) {
  const res = await fetch(process.env.NEXT_PUBLIC_API_URL + '/auth/token/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  if (!res.ok) throw new Error('Login failed');
  const data = await res.json();
  // store tokens in localStorage (use httpOnly cookies in production)
  localStorage.setItem('access', data.access);
  localStorage.setItem('refresh', data.refresh);
  return data;
}

export async function register(username, email, password) {
  const res = await fetch(process.env.NEXT_PUBLIC_API_URL + '/auth/register/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password })
  });
  if (!res.ok) throw new Error('Registration failed');
  return await res.json();
}

export function getAuthHeaders() {
  const token = localStorage.getItem('access');
  return token ? { 'Authorization': 'Bearer ' + token } : {};
}
