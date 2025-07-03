import { useContext } from 'react'
import SessionContext from '../SessionContext'

export default function AppHeader() {
  const [_, setSession] = useContext(SessionContext)

  return (
    <>
      <a href="#home" onClick={() => setSession({ page: 'home' })}>Beranda</a>
      &nbsp; &nbsp;
      <a href="#profile" onClick={() => setSession({ page: 'profile' })}>Profil</a>
      &nbsp; &nbsp;
      <a href="#contact" onClick={() => setSession({ page: 'contact' })}>Kontak</a>
      &nbsp; &nbsp;
      <a href="#contact" onClick={() => setSession({ page: 'login' })}>Login</a>
    </>
  )
}
