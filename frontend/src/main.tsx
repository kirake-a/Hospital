import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import PatientPage from './pages/PatientPage';
import './styles/index.css'

import { PrimeReactProvider } from 'primereact/api';
import 'primeflex/primeflex.css';
import 'primereact/resources/primereact.css';
import 'primereact/resources/themes/lara-light-indigo/theme.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Home />
  </StrictMode>,
)

export default function Home() {
  return (
    <PrimeReactProvider>
      <PatientPage />
    </PrimeReactProvider>
  )
}
