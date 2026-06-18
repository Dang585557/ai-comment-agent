import Link from "next/link";
import { useRouter } from "next/router";

const menus = [

    { title: "Dashboard", path: "/dashboard" },

    { title: "CEO Office", path: "/ceo" },

    { title: "AI Manager", path: "/manager" },

    { title: "Teams", path: "/teams" },

    { title: "Agents", path: "/agents" },

    { title: "Tasks", path: "/tasks" },

    { title: "Workflows", path: "/workflows" },

    { title: "Reports", path: "/reports" },

    { title: "Monitoring", path: "/monitoring" },

    { title: "Computer Lab", path: "/computer-lab" },

    { title: "Mobile Lab", path: "/mobile-lab" },

    { title: "Memory Center", path: "/memory" },

    { title: "Storage", path: "/storage" },

    { title: "Settings", path: "/settings" }

];

export default function Sidebar() {

    const router = useRouter();

    return (

        <aside className="w-72 bg-zinc-900 border-r border-zinc-800 h-screen">

            <div className="p-6 border-b border-zinc-800">

                <h1 className="text-2xl font-bold text-white">

                    AI-COMPANY

                </h1>

                <p className="text-zinc-400 text-sm mt-2">

                    CEO Command Center

                </p>

            </div>

            <div className="p-4 space-y-2">

                {menus.map((menu) => (

                    <Link
                        key={menu.path}
                        href={menu.path}
                        className={`block rounded-xl px-4 py-3 transition ${
                            router.pathname === menu.path
                                ? "bg-cyan-600 text-white"
                                : "text-zinc-300 hover:bg-zinc-800"
                        }`}
                    >

                        {menu.title}

                    </Link>

                ))}

            </div>

        </aside>

    );

}
