export const Navbar = () => {
    return (
        <div>
            <header className="bg-green-400 py-4">
                <div className="mx-auto ml-16 flex items-center">
                    <a href="/home" className="flex items-center hover:no-underline">
                        <img src="../logo.svg" alt="SourceManager" className="w-24 mr-4 ml-0"/>
                        <h1 className="text-white text-5xl">Source Manager</h1>
                    </a>
                </div>
            </header>
        </div>
    )
}