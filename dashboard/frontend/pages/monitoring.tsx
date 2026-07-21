import Link from "next/link";
export default function Page(){return <main style={{minHeight:'100vh',background:'#050a12',color:'#e6edf8',padding:24,fontFamily:'system-ui'}}><Link href="/dashboard">← Dashboard</Link><h1>Monitoring</h1><p>System health, CPU, RAM, Disk, Network, Agent Health, and Alert Status.</p></main>}
