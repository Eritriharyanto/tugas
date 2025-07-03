CREATE TABLE gejala (
  id INT PRIMARY KEY AUTO_INCREMENT,
  kode_gejala VARCHAR(10) NOT NULL UNIQUE,
  nama_gejala VARCHAR(100) NOT NULL
);

CREATE TABLE penyakit (
  id INT PRIMARY KEY AUTO_INCREMENT,
  kode VARCHAR(10) NOT NULL UNIQUE,
  nama_penyakit VARCHAR(100) NOT NULL,
  deskripsi TEXT
);

CREATE TABLE trimester (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nama_trimester VARCHAR(20) NOT NULL
);

CREATE TABLE pengguna (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nama VARCHAR(50) NOT NULL,
  no_hp VARCHAR(15),
  pekerjaan VARCHAR(50),
  alamat VARCHAR(100)
);

CREATE TABLE diagnosa (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_pengguna INT NOT NULL,
  id_trimester INT NOT NULL,
  id_penyakit INT NOT NULL,
  tanggal_diagnosa DATE NOT NULL,
  FOREIGN KEY (id_pengguna) REFERENCES pengguna(id),
  FOREIGN KEY (id_trimester) REFERENCES trimester(id),
  FOREIGN KEY (id_penyakit) REFERENCES penyakit(id)
);

CREATE TABLE diagnosis_gejala (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_diagnosa INT NOT NULL,
  id_gejala INT NOT NULL,
  FOREIGN KEY (id_diagnosa) REFERENCES diagnosa(id),
  FOREIGN KEY (id_gejala) REFERENCES gejala(id)
);

CREATE TABLE aturan (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_penyakit INT NOT NULL,
  id_gejala INT NOT NULL,
  FOREIGN KEY (id_penyakit) REFERENCES penyakit(id),
  FOREIGN KEY (id_gejala) REFERENCES gejala(id)
);


-- Insert trimester data
INSERT INTO trimester (nama_trimester) VALUES 
('Trimester 1'),
('Trimester 2'),
('Trimester 3');

-- Insert gejala data
INSERT INTO gejala (id, kode_gejala, nama_gejala) VALUES
(1, 'G01', 'Usia kehamilan kurang dari 16 minggu'),
(2, 'G02', 'Usia kehamilan kurang dari 20 minggu'),
(3, 'G03', 'Usia kehamilan lebih dari 20 minggu'),
(4, 'G04', 'Memiliki riwayat Preeklampsia pada kehamilan sebelumnya'),
(5, 'G05', 'Memiliki riwayat Diabetes Gestasional pada kehamilan sebelumnya'),
(6, 'G06', 'Memiliki riwayat kehamilan diluar kandungan sebelumnya'),
(7, 'G07', 'Memiliki riwayat hipertensi atau darah tinggi'),
(8, 'G08', 'Memiliki penyakit turunan darah tinggi dari keluarga'),
(9, 'G09', 'Memiliki riwayat diabetes dalam keluarga'),
(10, 'G10', 'Terjadi perdarahan pada usia kehamilan kurang dari 20 minggu'),
(11, 'G11', 'Terjadi perdarahan pada usia kehamilan lebih dari 22 minggu'),
(12, 'G12', 'Keluarnya darah tampak seperti flek darah'),
(13, 'G13', 'Perdarahan ringan berulang pada trimester dua atau tiga'),
(14, 'G14', 'Rahim terasa lebih besar dari usia kehamilan'),
(15, 'G15', 'Tingginya kadar hormon kehamilan (hCG)'),
(16, 'G16', 'Nyeri tajam di satu sisi perut bagian bawah'),
(17, 'G17', 'Perdarahan disertai gumpalan darah'),
(18, 'G18', 'Perdarahan tanpa nyeri perut'),
(19, 'G19', 'Tekanan atau rasa penuh pada panggul'),
(20, 'G20', 'Rasa tidak nyaman di perut bagian bawah'),
(21, 'G21', 'Keluhan pusing dan mual berlebihan'),
(22, 'G22', 'Perdarahan tanpa kontraksi rahim'),
(23, 'G23', 'Jaringan janin keluar tidak utuh dari jalan lahir'),
(24, 'G24', 'Rasa sakit dan nyeri pada perut bagian bawah'),
(25, 'G25', 'Nyeri pada tulang panggul'),
(26, 'G26', 'Nyeri atau kram pada panggul terus menerus dan memberat'),
(27, 'G27', 'Nyeri menjalar hingga bahu dan leher'),
(28, 'G28', 'Pusing terus menerus'),
(29, 'G29', 'Sakit kepala hebat seperti tertusuk-tusuk'),
(30, 'G30', 'Mual dan muntah'),
(31, 'G31', 'Mual dan muntah berlebih dan terus menerus (lebih dari 4x)'),
(32, 'G32', 'Kulit, bibir dan wajah terlihat pucat'),
(33, 'G33', 'Wajah terlihat pucat, pusing kepala, hingga pingsan'),
(34, 'G34', 'Wajah dan badan terlihat pucat kekuning-kuningan'),
(35, 'G35', 'Mengalami Jaundice (kulit dan mata menjadi kuning)'),
(36, 'G36', 'Kesulitan bernapas atau sesak napas'),
(37, 'G37', 'Tidur menggunakan 2-3 bantal untuk meredakan sesak napas'),
(38, 'G38', 'Detak jantung tidak teratur'),
(39, 'G39', 'Mudah lelah dan lesu'),
(40, 'G40', 'Mudah pingsan'),
(41, 'G41', 'Gangguan penglihatan (pandangan mata kabur, pandangan mata hilang secara sementara, berkunang-kunang)'),
(42, 'G42', 'Pembengkakan pada kaki'),
(43, 'G43', 'Pembengkakan pada bagian telapak kaki, wajah, dan tangan atau salah satu'),
(44, 'G44', 'Berat badan turun'),
(45, 'G45', 'Lidah mengering dan kotor'),
(46, 'G46', 'Mulut terasa kering'),
(47, 'G47', 'Rasa haus yang berlebih'),
(48, 'G48', 'Dehidrasi'),
(49, 'G49', 'Kenaikan suhu badan atau demam jika terjadi dehidrasi'),
(50, 'G50', 'Kenaikan suhu badan atau demam'),
(51, 'G51', 'Sensitif terhadap aroma tertentu'),
(52, 'G52', 'Mengeluarkan air liur secara berlebihan'),
(53, 'G53', 'Tangan gemetar dan berkeringat'),
(54, 'G54', 'Tekanan darah menjadi tinggi'),
(55, 'G55', 'Tidak ada tanda-tanda adanya janin/tidak merasakan gerakan janin'),
(56, 'G56', 'Rahim yang tampak lebih besar dari usia kandungan'),
(57, 'G57', 'Rasa sakit saat buang air kecil'),
(58, 'G58', 'Frekuensi buang air kecil meningkat'),
(59, 'G59', 'Urine yang keluar hanya sedikit'),
(60, 'G60', 'Cairan urine keruh'),
(61, 'G61', 'Nyeri pada bagian kandung kemih'),
(62, 'G62', 'Ada sensasi terbakar atau kram di perut bagian bawah'),
(63, 'G63', 'Teraba adanya jaringan (janin berwarna putih) pada gumpalan darah'),
(64, 'G64', 'Keluarnya jaringan tidak seluruhnya (tidak ada bagian dari plasenta, memungkinkan plasenta masih tertinggal di dalam)'),
(65, 'G65', 'Kontraksi berkurang setelah keluarnya jaringan (janin) berwarna putih.'),
(66, 'G66', 'Hilangnya tanda-tanda kehamilan misalnya tidak ada nyeri payudara, tidak ada mual-muntah (morning sickness)'),
(67, 'G67', 'Pada kondisi perdarahan hebat dapat menimbulkan gejala anemia (pusing, pandangan mata kabur, pingsan)');

-- Insert penyakit data
INSERT INTO penyakit (kode, nama_penyakit, deskripsi) VALUES
('P01', 'Anemia Kehamilan', 'cccccc'),
('P02', 'Preeklampsia','cccccc'),
('P03', 'Plasenta Previa','cccccc'),
('P04', 'Hiperemesis Gravidarum','cccccc'),
('P05', 'Kehamilan Ektopik','cccccc'),
('P06', 'Mola Hidatidosa','cccccc'),
('P07', 'Infeksi Saluran Kemih','cccccc'),
('P08', 'Diabetes Melitus Gestasional','cccccc'),
('P09', 'Abortus Imminens','cccccc'),
('P10', 'Abortus Inkomplit','cccccc');


-- Insert aturan (rules) for forward chaining
-- T1 
-- Hiperemesis Gravidarum (id_penyakit = 4)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(4, 30), -- Mual dan muntah
(4, 31), -- Mual dan muntah berlebih
(4, 52), -- Mengeluarkan air liur berlebihan
(4, 51), -- Sensitif terhadap aroma tertentu
(4, 47); -- Rasa haus berlebih


-- Abortus Imminens (id_penyakit = 9)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(9, 10), -- Perdarahan < 20 minggu
(9, 12), -- Keluar flek
(9, 24), -- Nyeri perut bawah
(9, 28), -- Pusing terus menerus
(9, 67); -- Gejala anemia


--  Kehamilan Ektopik (id_penyakit = 5)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(5, 26), -- Nyeri/kram panggul berat
(5, 27), -- Nyeri menjalar
(5, 10), -- Perdarahan < 20 minggu
(5, 63), -- Teraba jaringan janin
(5, 65); -- Kontraksi berkurang

-- T2
-- Preeklampsia (id_penyakit = 2)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(2, 41), -- Gangguan penglihatan
(2, 42), -- Pembengkakan kaki
(2, 43), -- Pembengkakan wajah/tangan
(2, 54), -- Tekanan darah tinggi
(2, 29); -- Sakit kepala hebat


--  Anemia Kehamilan (id_penyakit = 1)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(1, 32), -- Wajah pucat
(1, 33), -- Pingsan, pucat
(1, 34), -- Kekuningan
(1, 67), -- Gejala anemia
(1, 28); -- Pusing

--  Infeksi Saluran Kemih (id_penyakit = 7)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(7, 57), -- Nyeri saat buang air
(7, 58), -- Frekuensi meningkat
(7, 59), -- Urine sedikit
(7, 60), -- Urine keruh
(7, 61), -- Nyeri kandung kemih
(7, 62); -- Sensasi terbakar/kram

-- T3
-- Plasenta Previa (id_penyakit = 3)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(3, 11), -- Perdarahan > 22 minggu
(3, 66), -- Hilangnya tanda kehamilan
(3, 56), -- Rahim besar
(3, 55), -- Tidak ada gerakan janin
(3, 64); -- Jaringan tidak keluar semua

-- Mola Hidatidosa (id_penyakit = 6)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(6, 56), -- Rahim besar
(6, 55), -- Tidak terasa janin
(6, 49), -- Demam karena dehidrasi
(6, 65), -- Kontraksi hilang
(6, 63); -- Jaringan janin putih

-- Diabetes Melitus Gestasional (id_penyakit = 8)
INSERT INTO aturan (id_penyakit, id_gejala) VALUES
(8, 45), -- Lidah kering
(8, 46), -- Mulut kering
(8, 47), -- Haus berlebih
(8, 48), -- Dehidrasi
(8, 54); -- Tekanan darah tinggi
