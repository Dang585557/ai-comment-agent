import { ReactNode } from "react";
import Link from "next/link";

interface Props {
    children: ReactNode;
}

const menus = [
    { name: "Dashboard", href: "/dashboard" },
    { name: "CEO Office", href: "/ceo" },
    { name: "AI Manager", href: "/manager" },
    { name: "Teams", href: "/teams" },
    { name: "Agents", href: "/agents" },
    { name: "Tasks", href: "/tasks" },
    { name: "Workflows", href: "/workflows" },
    { name: "Reports", href: "/reports" },
    { name: "Monitoring", href: "/monitoring" },
    { name: "Computer Lab", href: "/computer-lab" },
    { name: "Mobile Lab", href: "/mobile-lab" },
    { name: "Memory Center", href: "/memory" },
    { name: "Storage", href: "/storage" },
    { name: "Settings", href: "/settings" },
];

export default function DashboardLayout({ children }: Props) {

    return (

        <div className="min-h-screen bg-zinc-950 text-white flex">

            <aside className="w-72 border-r border-zinc-800 bg-zinc-900">

                <div className="p-6 border-b border-zinc-800">

                    <h1 className="text-2xl font-bold">
                        AI-COMPANY
                    </h1>

                    <p className="text-zinc-400 text-sm mt-2">
                        CEO Command Center
                    </p>

                </div>

                <nav className="p-4 space-y-2">

                    {menus.map((menu) => (

                        <Link
                            key={menu.href}
                            href={menu.href}
                            className="block rounded-lg px-4 py-3 hover:bg-zinc-800 transition"
                        >
                            {menu.name}
                        </Link>

                    ))}

                </nav>

            </aside>

            <main className="flex-1 flex flex-col">

                <header className="h-20 border-b border-zinc-800 flex items-center justify-between px-8 bg-zinc-900">

                    <div>

                        <h2 className="text-2xl font-bold">

                            AI Company Dashboard

                        </h2>

                        <p className="text-green-400 text-sm">

                            ● System Online

                        </p>

                    </div>

                    <div className="flex items-center gap-8">

                        <div>

                            {new Date().toLocaleString()}

                        </div>

                        <div className="text-right">

                            <p className="font-semibold">

                                CEO

                            </p>

                            <p className="text-sm text-zinc-400">

                                Administrator

                            </p>

                        </div>

                    </div>

                </header>

                <div className="flex-1 p-8 overflow-auto">

                    {children}

                </div>

            </main>

        </div>

    );

}
