import { useContext } from 'react'
import SessionContext from '../SessionContext'

export default function Error() {
  const [session, setSession] = useContext(SessionContext)

  return (
    <>
      <h1>Halaman Error</h1>
      <p>Halaman "{session.page}" tidak ditemukan.</p>
      <a href="#home" onClick={() => setSession({ page: 'home' })}>Kembali ke beranda</a>
    </>
  )
}
