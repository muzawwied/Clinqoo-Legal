# -*- coding: utf-8 -*-
NAV = """<header class="nav"><div class="nav-in"><a class="brand" href="/Clinqoo-Legal/">Clinqoo</a><nav>
<a href="/Clinqoo-Legal/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
<a href="/Clinqoo-Legal/kebijakan-privasi.html">Kebijakan Privasi</a>
<a href="/Clinqoo-Legal/kebijakan-cookie.html">Cookie</a>
<a href="/Clinqoo-Legal/kebijakan-pembayaran.html">Pembayaran</a>
</nav></div></header>"""
FOOT = """<footer><div class="wrap"><p class="sub">&copy; 2026 Clinqoo. Dokumen legalitas resmi platform Clinqoo. Pertanyaan: muzawwied@gmail.com</p>
<div class="flinks">
<a href="/Clinqoo-Legal/syarat-ketentuan.html">Syarat &amp; Ketentuan</a>
<a href="/Clinqoo-Legal/kebijakan-privasi.html">Kebijakan Privasi</a>
<a href="/Clinqoo-Legal/kebijakan-cookie.html">Kebijakan Cookie</a>
<a href="/Clinqoo-Legal/kebijakan-pembayaran.html">Kebijakan Pembayaran</a>
</div></div></footer>"""
def page(title, desc, body, updated="14 September 2026"):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="robots" content="index,follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" sizes="64x64" href="/Clinqoo-Legal/favicon.png">
<link rel="apple-touch-icon" href="/Clinqoo-Legal/icon-180.png">
<link property="og:image" content="https://muzawwied.github.io/Clinqoo-Legal/icon-512.png">
<link rel="stylesheet" href="/Clinqoo-Legal/style.css">
</head>
<body>
{NAV}
<main><div class="wrap">
{body}
</div></main>
{FOOT}
</body>
</html>"""

INDEX = """<h1>Dokumen Legalitas Clinqoo</h1>
<p class="sub">Selamat datang di pusat dokumen hukum Clinqoo. Dengan menggunakan Clinqoo &mdash; mulai dari membuat dan menerbitkan situs, mengisi saldo, hingga fitur AI &mdash; kamu dianggap telah membaca dan menyetujui dokumen di bawah ini.</p>
<div class="docs-list">
<a href="/Clinqoo-Legal/syarat-ketentuan.html"><b>Syarat &amp; Ketentuan</b><span>Aturan penggunaan platform Clinqoo: akun, konten, situs yang diterbitkan, fitur AI, dan batasan tanggung jawab.</span></a>
<a href="/Clinqoo-Legal/kebijakan-privasi.html"><b>Kebijakan Privasi</b><span>Data apa yang kami kumpulkan, bagaimana kami menggunakannya, dan bagaimana kamu meminta penghapusan data.</span></a>
<a href="/Clinqoo-Legal/kebijakan-cookie.html"><b>Kebijakan Cookie</b><span>Cookie dan penyimpanan lokal (localStorage) yang dipakai Clinqoo agar pengalamanmu tetap nyaman.</span></a>
<a href="/Clinqoo-Legal/kebijakan-pembayaran.html"><b>Kebijakan Pembayaran</b><span>Top up saldo, pembayaran QRIS, kuota AI, langganan, serta ketentuan pengembalian dana.</span></a>
</div>
<hr>
<h2>Kontak</h2>
<p>Untuk pertanyaan seputar dokumen ini, permintaan penghapusan data, atau pelanggaran konten, hubungi kami di <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a>. Kami menanggapi maksimal 2&times;24 jam kerja.</p>
<p>Terakhir diperbarui: 14 September 2026.</p>"""

SK = """<h1>Syarat &amp; Ketentuan</h1>
<p class="sub">Dokumen ini mengatur penggunaan layanan Clinqoo oleh seluruh pengguna.</p>
<div class="toc">
<a href="#1">1. Definisi</a>
<a href="#2">2. Akun &amp; Keamanan</a>
<a href="#3">3. Layanan Publikasi Situs</a>
<a href="#4">4. Fitur AI (Clinqoo AI &amp; Mode Agent)</a>
<a href="#5">5. Konten yang Dilarang</a>
<a href="#6">6. Saldo, Kuota &amp; Pembayaran</a>
<a href="#7">7. Komunitas</a>
<a href="#8">8. Kepemilikan &amp; Lisensi Konten</a>
<a href="#9">9. Batasan Tanggung Jawab</a>
<a href="#10">10. Perubahan Layanan &amp; Dokumen</a>
<a href="#11">11. Pengakhiran</a>
<a href="#12">12. Hukum yang Berlaku</a>
</div>
<hr>
<h2 id="1">1. Definisi</h2>
<p>&ldquo;Clinqoo&rdquo; adalah platform yang memungkinkan pengguna membangun, mengedit, dan menerbitkan situs web secara langsung dari browser, termasuk fitur workspace, template, integrasi GitHub &amp; Cloudflare, dompet digital, serta asisten AI. &ldquo;Pengguna&rdquo; adalah setiap orang yang mengakses atau menggunakan Clinqoo, baik tanpa akun (pengunjung) maupun dengan akun (anggota).</p>
<h2 id="2">2. Akun &amp; Keamanan</h2>
<ul>
<li>Kamu wajib memberikan data yang benar saat mendaftar dan menjaga kerahasiaan kredensial akunmu sendiri.</li>
<li>Semua aktivitas yang terjadi melalui akunmu dianggap dilakukan oleh kamu. Segera laporkan ke <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a> jika ada akses yang tidak kamu kenali.</li>
<li>Kami berhak membatasi atau menonaktifkan akun yang menunjukkan aktivitas mencurigakan, penyalahgunaan kuota, atau pelanggaran dokumen ini.</li>
<li>Akun yang tidak aktif dalam jangka panjang dapat dihapus setelah pemberitahuan melalui email.</li>
</ul>
<h2 id="3">3. Layanan Publikasi Situs</h2>
<ul>
<li>Situs yang kamu buat diterbitkan melalui jalur deploy (GitHub/Cloudflare Pages atau sejenisnya). Kamu bertanggung jawab penuh atas isi situs yang kamu terbitkan.</li>
<li>Kami tidak menjamin situs selalu bebas gangguan. Pemeliharaan, pembaruan, atau kegagalan pihak ketiga (hosting, DNS, repository) dapat memengaruhi ketersediaan situs.</li>
<li>Domain kustom, pengaturan akses, dan konfigurasi deploy adalah kendali kamu; kesalahan konfigurasi di luar kendali teknis kami bukan tanggung jawab kami.</li>
<li>Kami dapat menghentikan penayangan situs yang melanggar hukum Indonesia atau dokumen ini.</li>
</ul>
<h2 id="4">4. Fitur AI (Clinqoo AI &amp; Mode Agent)</h2>
<ul>
<li>Output AI bersifat bantu/saran. Verifikasi seluruh kode, teks, dan hasil AI sebelum dipublikasikan; kami tidak menjamin output AI bebas dari kesalahan.</li>
<li>Penggunaan fitur AI tunduk pada kuota harian sesuai paket. Upaya melewati kuota dengan cara apa pun (multi-akun, otomatisasi, manipulasi) dapat menyebabkan pembatasan atau penutupan akun.</li>
<li>Jangan memasukkan data rahasia, kredensial, atau data pribadi pihak ketiga ke dalam fitur AI.</li>
</ul>
<h2 id="5">5. Konten yang Dilarang</h2>
<p>Kamu dilarang keras membuat, menerbitkan, atau menyimpan di Clinqoo konten yang berkaitan dengan:</p>
<ul>
<li>Judi online dalam bentuk apa pun, pencucian uang, atau skema penipuan (termasuk investasi bodong dan ponzi);</li>
<li>Narkotika, psikotropika, dan zat terlarang;</li>
<li>Perdagangan barang/jasa ilegal, pemalsuan dokumen, atau pelanggaran hak kekayaan intelektual;</li>
<li>Konten pornografi dan eksploitasi anak (Konten ini dilaporkan sesuai UU No. 19/2016);</li>
<li>Ujaran kebencian, hasutan, atau konten yang mengancam keselamatan orang lain;</li>
<li>Malware, phishing, atau upaya merusak sistem.</li>
</ul>
<p>Pelanggaran mengakibatkan penghapusan konten dan/atau pemblokiran akun permanen, dan dapat dilaporkan kepada aparat berwenang.</p>
<h2 id="6">6. Saldo, Kuota &amp; Pembayaran</h2>
<ul>
<li>Saldo Clinqoo bersifat prabayar dan digunakan untuk layanan berbayar di dalam platform (mis. kuota AI, layanan premium).</li>
<li>Pengisian saldo dilakukan melalui QRIS dengan penyedia pembayaran pihak ketiga. Konfirmasi pembayaran otomatis melalui webhook bertanda tangan digital.</li>
<li>Detail biaya, metode, dan pengembalian dana diatur dalam <a href="/Clinqoo-Legal/kebijakan-pembayaran.html">Kebijakan Pembayaran</a>.</li>
</ul>
<h2 id="7">7. Komunitas</h2>
<ul>
<li>Fitur komunitas hanya boleh digunakan untuk interaksi yang sehat, relevan, dan menghormati sesama pengguna.</li>
<li>Kami dapat menghapus postingan/komentar yang mengandung spam, ujaran kebencian, promosi ilegal, atau konten terlarang pasal 5.</li>
</ul>
<h2 id="8">8. Kepemilikan &amp; Lisensi Konten</h2>
<ul>
<li>Konten milikmu tetap milikmu. Dengan menerbitkan melalui Clinqoo, kamu memberi kami lisensi terbatas untuk menyimpan, memproses, dan menayangkan konten tersebut sepanjang diperlukan untuk menjalankan layanan.</li>
<li>Logo, nama, dan antarmuka Clinqoo adalah milik kami dan tidak boleh digunakan tanpa izin.</li>
<li>Dokumen ini dilindungi hak cipta &mdash; menyalin bagian besar tanpa atribut untuk tujuan komersial tidak diperkenankan.</li>
</ul>
<h2 id="9">9. Batasan Tanggung Jawab</h2>
<p>Layanan disediakan &ldquo;sebagaimana adanya&rdquo;. Sepanjang diizinkan hukum, Clinqoo tidak bertanggung jawab atas kerugian tidak langsung, kehilangan data, kehilangan pendapatan, atau sengketa antara pengguna dan pihak ketiga. Tanggung jawab kami maksimal setara nilai yang telah kamu bayarkan kepada Clinqoo dalam 6 (enam) bulan terakhir.</p>
<h2 id="10">10. Perubahan Layanan &amp; Dokumen</h2>
<p>Kami dapat memperbarui fitur, kuota, harga, maupun dokumen ini. Perubahan penting diumumkan di dalam platform atau melalui email. Lanjut menggunakan Clinqoo setelah perubahan berlaku berarti kamu menyetujuinya.</p>
<h2 id="11">11. Pengakhiran</h2>
<p>Kamu dapat berhenti kapan saja dengan menghapus akunmu. Kami dapat mengakhiri akses atas pelanggaran berat (pasal 5) atau tunggakan pembayaran. Sisa saldo yang memenuhi syarat Kebijakan Pembayaran dapat diajukan untuk pengembalian.</p>
<h2 id="12">12. Hukum yang Berlaku</h2>
<p>Dokumen ini tunduk pada hukum Republik Indonesia. Segala sengketa diselesaikan secara musyawarah, dan bila tidak tercapai, melalui pengadilan yang berwenang di Indonesia. Pengguna diwajibkan mematuhi UU ITE (No. 11/2008 jo. No. 19/2016), UU PDP (No. 27/2022), dan peraturan pelaksananya.</p>"""

PRIV = """<h1>Kebijakan Privasi</h1>
<p class="sub">Kami menghormati privasimu. Dokumen ini menjelaskan data yang dikumpulkan Clinqoo dan hak-hak kamu sesuai UU Perlindungan Data Pribadi (UU No. 27/2022).</p>
<div class="toc">
<a href="#kumpul">Data yang Kami Kumpulkan</a>
<a href="#pakai">Cara Kami Menggunakan Data</a>
<a href="#pihak3">Pembagian kepada Pihak Ketiga</a>
<a href="#simpan">Penyimpanan &amp; Keamanan</a>
<a href="#retensi">Retensi</a>
<a href="#hak">Hak Kamu &amp; Penghapusan Data</a>
<a href="#anak">Privasi Anak</a>
</div>
<hr>
<h2 id="kumpul">Data yang Kami Kumpulkan</h2>
<ul>
<li><b>Data akun:</b> nama, email, kata sandi (ter-hash), foto profil opsional, dan preferensi pengaturan.</li>
<li><b>Data penggunaan:</b> proyek yang kamu buat, file workspace, riwayat chat, aktivitas top up, dan log teknis (IP, jenis perangkat, waktu akses).</li>
<li><b>Data pembayaran:</b> nominal dan status transaksi top up. Kami <b>tidak menyimpan</b> data kartu/kredensial pembayaran &mdash; pembayaran QRIS diproses penyedia pihak ketiga.</li>
<li><b>Data yang kamu kirim ke fitur AI:</b> isi percakapan/kode diproses untuk menghasilkan jawaban dan, bila diperlukan, diteruskan ke penyedia model AI.</li>
</ul>
<h2 id="pakai">Cara Kami Menggunakan Data</h2>
<ul>
<li>Menjalankan dan mempersonalisasi layanan (akun, proyek, dompet, kuota).</li>
<li>Memproses pembayaran dan mencegah penyalahgunaan kuota/penipuan.</li>
<li>Mengirim pemberitahuan penting terkait akun dan layanan.</li>
<li>Meningkatkan kualitas produk berdasarkan pola penggunaan agregat.</li>
</ul>
<p>Kami tidak menjual data pribadimu kepada siapa pun.</p>
<h2 id="pihak3">Pembagian kepada Pihak Ketiga</h2>
<p>Data hanya dibagikan sebatas yang diperlukan kepada:</p>
<ul>
<li>Penyedia hosting &amp; basis data (Cloudflare, GitHub) untuk menyimpan dan menerbitkan situs;</li>
<li>Penyedia pembayaran QRIS untuk memverifikasi transaksi;</li>
<li>Penyedia model AI untuk memproses permintaan fitur AI.</li>
</ul>
<p>Masing-masing diproses hanya untuk fungsinya, dan kami tidak mengizinkan mereka memakai datamu untuk tujuan lain.</p>
<h2 id="simpan">Penyimpanan &amp; Keamanan</h2>
<p>Data disimpan di infrastruktur Cloudflare dengan akses terbatas. Kami menerapkan autentikasi token, verifikasi tanda tangan digital pada webhook pembayaran, dan enkripsi saat transit (HTTPS). Tidak ada sistem yang 100% aman; segera lapor ke <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a> bila kamu menemukan celah.</p>
<h2 id="retensi">Retensi</h2>
<p>Data akun disimpan selama akunmu aktif. Setelah penghapusan akun, data pribadi dihapus maksimal 30 hari, kecuali data transaksi yang wajib disimpan menurut regulasi (maksimal 5 tahun) dalam bentuk teranimasi.</p>
<h2 id="hak">Hak Kamu &amp; Penghapusan Data</h2>
<ul>
<li>Melihat, memperbaiki, atau menghapus data pribadimu sendiri melalui halaman akun.</li>
<li>Meminta salinan atau penghapusan seluruh data terkait akunmu dengan email ke <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a> (diproses maks. 14 hari kerja).</li>
<li>Menarik persetujuan pemrosesan tertentu, dengan konsekuensi fitur terkait tidak dapat berjalan.</li>
</ul>
<h2 id="anak">Privasi Anak</h2>
<p>Clinqoo tidak ditujukan untuk anak di bawah 13 tahun. Bila kami menemukan data anak tanpa persetujuan orang tua/wali, kami menghapusnya.</p>"""

COOKIE = """<h1>Kebijakan Cookie</h1>
<p class="sub">Clinqoo memakai cookie dan penyimpanan lokal (localStorage) dalam jumlah kecil agar fitur tetap berfungsi.</p>
<hr>
<h2>Jenis yang Kami Gunakan</h2>
<ul>
<li><b>Autentikasi (wajib):</b> token sesi di localStorage (&ldquo;clinqoo_auth_token&rdquo; dan sejenisnya) untuk menjaga kamu tetap masuk. Tanpa ini, fitur akun tidak berfungsi.</li>
<li><b>Preferensi (fungsional):</b> mode gelap/terang, mode chat terakhir dipilih, cache 5 menit halaman tertentu agar navigasi terasa cepat.</li>
<li><b>Data lokal proyek (fungsional):</b> file workspace, draft chat, dan status order top up sementara, agar pekerjaanmu tidak hilang saat halaman dimuat ulang.</li>
</ul>
<h2>Yang Kami Tidak Gunakan</h2>
<ul>
<li>Tidak memakai cookie iklan atau pelacak lintas situs pihak ketiga.</li>
<li>Tidak menjual data penelusuranmu.</li>
</ul>
<h2>Mengelola Cookie</h2>
<p>Kamu bisa menghapus penyimpanan lokal kapan pun dari pengaturan browser. Namai dengan hati-hati: menghapus token autentikasi akan mengeluarkan kamu dari akun dan draft lokal bisa hilang.</p>"""

PAY = """<h1>Kebijakan Pembayaran</h1>
<p class="sub">Ketentuan top up saldo, kuota, langganan, dan pengembalian dana di Clinqoo.</p>
<div class="toc">
<a href="#topup">Top Up Saldo</a>
<a href="#harga">Harga, Biaya &amp; Kuota</a>
<a href="#refund">Pengembalian Dana</a>
<a href="#banned">Penutupan Akun &amp; Saldo</a>
<a href="#sengketa">Sengketa Transaksi</a>
</div>
<hr>
<h2 id="topup">Top Up Saldo</h2>
<ul>
<li>Top up minimal Rp10.000 dan dilakukan melalui QRIS &mdash; didukung GoPay, OVO, DANA, ShopeePay, dan seluruh m-banking di Indonesia.</li>
<li>Pembayaran diproses oleh penyedia QRIS resmi (BuatQris). Konfirmasi masuk otomatis real-time melalui webhook bertanda tangan digital; saldo ditambahkan setelah verifikasi berhasil.</li>
<li>Jika saldo belum masuk padahal dana terpotong, tunggu maksimal 5 menit lalu hubungi <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a> dengan bukti transaksi (nominal, waktu, dan order ID seperti TOPUPQ-xxx).</li>
</ul>
<h2 id="harga">Harga, Biaya &amp; Kuota</h2>
<ul>
<li>Harga dan kuota layanan (mis. kuota AI harian gratis 25, paket Pro, dll.) tercantum di halaman masing-masing dan dapat berubah; perubahan diumumkan di dalam platform.</li>
<li>Biaya layanan QRIS mengikuti tarif penyedia pembayaran (mulai 1% per transaksi berhasil). Transaksi pending, gagal, atau kedaluwarsa tidak dikenakan biaya.</li>
<li>Saldo yang sudah dibeli hanya dapat dipakai untuk layanan di dalam Clinqoo dan tidak dapat dipindahtangankan ke pengguna lain.</li>
</ul>
<h2 id="refund">Pengembalian Dana</h2>
<ul>
<li><b>Transaksi top up:</b> dana yang berhasil masuk ke saldo bersifat final. Pengembalian dipertimbangkan hanya untuk kesalahan sistem (saldo tidak masuk padahal dana terpotong) dengan bukti yang lengkap, diproses maks. 7 hari kerja ke rekening asal.</li>
<li><b>Transaksi yang dibatalkan atau kedaluwarsa:</b> tidak dikenakan biaya apa pun; dana tidak terpotong.</li>
<li><b>Kuota/langganan:</b> langganan yang sudah aktif tidak dapat di-refund untuk sisa masa berlaku, kecuali ada gangguan layanan berat dari sisi kami.</li>
</ul>
<h2 id="banned">Penutupan Akun &amp; Saldo</h2>
<p>Akun yang kami tutup karena pelanggaran berat (judi, penipuan, konten ilegal) tidak mendapatkan pengembalian saldo. Akun yang kamu tutup sendiri dapat mengajukan pengembalian sisa saldo di atas Rp10.000 ke rekeningmu, diproses maks. 7 hari kerja.</p>
<h2 id="sengketa">Sengketa Transaksi</h2>
<p>Sampaikan dulu kepada tim kami di <a href="mailto:muzawwied@gmail.com">muzawwied@gmail.com</a> sebelum mengajukan chargeback ke bank/e-wallet. Chargeback yang terbukti disengaja tanpa upaya penyelesaian dapat menyebabkan akun ditangguhkan.</p>"""

open('index.html','w').write(page("Clinqoo — Dokumen Legalitas", "Syarat & Ketentuan, Kebijakan Privasi, Cookie, dan Pembayaran Clinqoo. Terbuka untuk umum tanpa login.", INDEX))
open('syarat-ketentuan.html','w').write(page("Syarat & Ketentuan — Clinqoo", "Aturan penggunaan platform Clinqoo: akun, publikasi situs, fitur AI, konten terlarang, dan batasan tanggung jawab.", SK))
open('kebijakan-privasi.html','w').write(page("Kebijakan Privasi — Clinqoo", "Data yang dikumpulkan Clinqoo, penggunaannya, hak kamu atas data pribadi, dan cara penghapusannya sesuai UU PDP.", PRIV))
open('kebijakan-cookie.html','w').write(page("Kebijakan Cookie — Clinqoo", "Cookie dan localStorage yang dipakai Clinqoo — tanpa cookie iklan atau pelacak pihak ketiga.", COOKIE))
open('kebijakan-pembayaran.html','w').write(page("Kebijakan Pembayaran — Clinqoo", "Top up QRIS, biaya layanan, kuota, dan ketentuan pengembalian dana Clinqoo.", PAY))
print("5 halaman legal + index dibuat")
