const cards = [

    {
        title: "Total Agents",
        value: "25",
        color: "text-cyan-400",
    },

    {
        title: "Active Tasks",
        value: "12",
        color: "text-yellow-400",
    },

    {
        title: "Completed Today",
        value: "87",
        color: "text-green-400",
    },

    {
        title: "System Health",
        value: "99.9%",
        color: "text-emerald-400",
    },

    {
        title: "Storage Used",
        value: "235 GB",
        color: "text-purple-400",
    },

    {
        title: "API Calls Today",
        value: "13,842",
        color: "text-pink-400",
    },

];

export default function SummaryCards() {

    return (

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

            {cards.map((card) => (

                <div
                    key={card.title}
                    className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 hover:border-cyan-500 transition"
                >

                    <p className="text-zinc-400 text-sm">

                        {card.title}

                    </p>

                    <h2 className={`text-3xl font-bold mt-3 ${card.color}`}>

                        {card.value}

                    </h2>

                </div>

            ))}

        </div>

    );

}
