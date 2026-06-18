export default function QuickActions() {

    const actions = [

        {
            title: "New Task",
            color: "bg-cyan-600 hover:bg-cyan-500",
        },

        {
            title: "Generate Report",
            color: "bg-green-600 hover:bg-green-500",
        },

        {
            title: "System Backup",
            color: "bg-purple-600 hover:bg-purple-500",
        },

        {
            title: "System Settings",
            color: "bg-orange-600 hover:bg-orange-500",
        },

    ];

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-2xl font-bold mb-6">

                Quick Actions

            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">

                {actions.map((action) => (

                    <button
                        key={action.title}
                        className={`${action.color} rounded-xl p-5 font-semibold transition duration-300`}
                    >

                        {action.title}

                    </button>

                ))}

            </div>

        </div>

    );

}
