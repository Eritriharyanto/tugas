import { createContext, useState } from 'react'

const SessionContext = createContext({ })

export function SessionProvider({ children }) {
  const session = useState({ page: 'home' })

  return (
    <SessionContext.Provider value={session}>
      {children}
    </SessionContext.Provider>
  )
}

export default SessionContext
