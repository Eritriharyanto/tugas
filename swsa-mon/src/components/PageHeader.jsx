export default function PageHeader({ page, onClickMenu }) {
  const menu = {
    home: "Home",
    gallery: "Gallery",
    about: "About",
  };
  return (
    <header className='mb-auto pb-1'>
      <div>
        <h3 className='float-md-start mb-0'>Summoners War Monsters</h3>
        <nav className='nav nav-menu justify-content-center float-md-end'>
          {Object.entries(menu).map(([key, value], index) => {
            const isActive = key == page;
            const active = isActive ? "active" : "";
            return (
              <a
                key={index}
                className={`nav-link fw-bold py-1 px-0 ${active}`}
                href={`#${key}`}
                aria-current={isActive ? "page" : null}
                onClick={onClickMenu(key)}
              >
                {value}
              </a>
            );
          })}
        </nav>
      </div>
    </header>
  );
}
