function Header() {
  return (
    <header className="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-xl border-b border-outline-variant/10">
      <div className="h-16 w-full px-lg flex items-center justify-between max-w-[1200px] mx-auto">
        <div className="flex items-center gap-sm">
          <img src="/atlas-logo.png" alt="Atlas" className="w-8 h-8 rounded-lg" />
          <span className="font-headline-md text-headline-md tracking-tight text-on-surface">
            Atlas
          </span>
        </div>
      </div>
    </header>
  );
}

export default Header;
