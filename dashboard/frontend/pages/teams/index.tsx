import Link from "next/link";
const teams=['tiktok','video','developer','research','website'];
export default function Page(){return <main style={{minHeight:'100vh',background:'#050a12',color:'#e6edf8',padding:24,fontFamily:'system-ui'}}><Link href="/dashboard">← Dashboard</Link><h1>Teams</h1>{teams.map(t=><p key={t}><Link href={`/teams/${t}`}>{t.toUpperCase()} Team</Link></p>)}</main>}
