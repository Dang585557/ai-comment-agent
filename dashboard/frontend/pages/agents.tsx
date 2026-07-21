import Link from "next/link";
export default function Page(){return <main style={{minHeight:'100vh',background:'#050a12',color:'#e6edf8',padding:24,fontFamily:'system-ui'}}><Link href="/dashboard">← Dashboard</Link><h1>Agents</h1><p>All active AI workers and operating status.</p></main>}
