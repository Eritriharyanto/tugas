const About = () => {
  return (
    <section className='py-5 text-center'>
      <div className='container'>
        <h2 className='mb-4'>About</h2>
        <div className='d-flex flex-column align-items-center'>
          <img
            src='/images/WhatsApp Image 2025-05-01 at 11.06.20.jpeg'
            className='rounded-circle mb-3'
            style={{
              width: "150px",
              height: "150px",
              objectFit: "cover",
            }}
          />
          <h4>Eri</h4>
          <p className='text-muted'>
            Halo Saya Eri Mahasiswa Informatika Universitas Jenderal Achmad Yani Yogyakarta angkatan 2023 yang sedang belajar React JS pertama kali nya dan pengembangan
            web modern. Proyek ini dibuat sebagai latihan membangun aplikasi
            Pokédex sederhana dengan routing dan pengelolaan data lokal.
            Maaf Pemula.
          </p>
          <a
            href='https://github.com/Eritriharyanto'
            target='_blank'
            rel='noopener noreferrer'
            className='btn btn-outline-dark mt-2'
          >
            🔗 Kunjungi GitHub Saya
          </a>
        </div>
      </div>
    </section>
  );
};

export default About;
