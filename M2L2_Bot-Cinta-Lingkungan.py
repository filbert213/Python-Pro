import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! Aku robot pencinta lingkungan!')

@bot.command()
async def pilah(ctx, *, benda: str):
    data = {
        "botol plastik": "plastik",
        "tutup botol": "plastik",
        "kemasan makanan": "plastik",
        "tas plastik": "plastik",
        "kardus": "kertas",
        "koran bekas": "kertas",
        "majalah bekas": "kertas",
        "robekan kertas": "kertas",
        "gelas": "kaca",
        "botol kaca": "kaca",
        "pecahan kaca": "kaca",
        "kulit buah": "sisa makanan",
        "sisa sayur": "sisa makanan",
        "tulang": "sisa makanan",
        "elektronik rusak": "logam",
        "baterai": "logam",
        "tutup botol besi": "logam",
        "kaleng": "logam",
        "paku": "logam"
    }
    if benda.lower() in data:
        kategori = data[benda.lower()]
        await ctx.send(f'{benda} termasuk kategori sampah {kategori}.')
    else:
        await ctx.send(f'{benda} tidak ditemukan di database.')

@bot.command()
async def buang(ctx, *, benda: str):
    data = {
        "botol plastik": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "tutup botol": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "kemasan makanan": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "tas plastik": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "kardus": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "koran bekas": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "majalah bekas": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "robekan kertas": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "gelas": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "botol kaca": "anorganik, jadi harusnya dibuang ke tempat sampah anorganik yang berwarna kuning",
        "pecahan kaca": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah",
        "kulit buah": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "sisa sayur": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "tulang": "organik, jadi harusnya dibuang ke tempat sampah organik yang berwarna hijau",
        "elektronik rusak": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah",
        "baterai": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah",
        "tutup botol besi": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah",
        "kaleng": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah",
        "paku": "b3, jadi harusnya dibuang ke tempat sampah b3 yang berwarna merah"
    }
    if benda.lower() in data:
        jenis = data[benda.lower()]
        await ctx.send(f'{benda} termasuk jenis sampah {jenis}.')
    else:
        await ctx.send(f'{benda} tidak ditemukan di database.')

@bot.command()
async def fakta(ctx):
    fakta = [
        "🌱Sampah organik dapat terurai secara alami dan biasanya berasal dari sisa makanan atau bahan-bahan yang dapat terurai seperti daun dan kayu.",
        "Sampah anorganik adalah sampah yang tidak dapat terurai secara alami, seperti plastik, logam, dan kaca.",
        "🪫Sampah B3 (Bahan Berbahaya dan Beracun) memerlukan penanganan khusus karena dapat membahayakan kesehatan manusia dan lingkungan, contohnya adalah baterai dan elektronik rusak.",
        "♻️Daur ulang sampah anorganik seperti plastik dan kertas📄 dapat mengurangi jumlah sampah di tempat pembuangan akhir dan menghemat sumber daya alam.",
        "Komposting adalah proses mengubah sampah organik menjadi pupuk alami🪏 yang dapat digunakan untuk menyuburkan tanaman.",
        "🗑️Selain tempat sampah organik (hijau), anorganik (kuning), dan B3 (merah), ada juga tempat sampah untuk sampah residu (abu-abu) dan tempat sampah spesifik kertas (biru).",
        "Terdapat perkembangan teknologi yang memungkinkan pengolahan sampah menjadi energi⚡️, seperti insinerasi dan biogas.",
        "Sudah mulai ada plastik biodegradable yang dapat terurai lebih cepat dibandingkan plastik konvensional."
    ]
    fakta = random.choice(fakta)
    await ctx.send(f'Fakta Sampah: {fakta}')

@bot.command()
async def diy(ctx, *, benda: str):
    data = {
        "botol plastik": "dapat dibuat menjadi pot bunga atau tempat pensil",
        "tutup botol": "dapat dibuat menjadi gantungan kunci atau hiasan dinding",
        "kemasan makanan": "dapat dibuat menjadi dompet atau tas kecil",
        "tas plastik": "dapat dibuat menjadi dompet atau tas kecil",
        "kardus": "dapat dibuat menjadi tempat pensil atau hiasan dinding",
        "koran bekas": "dapat dibuat menjadi tempat pensil atau hiasan meja",
        "majalah bekas": "dapat dibuat menjadi tempat pensil atau hiasan meja",
        "robekan kertas": "dapat dibuat menjadi tempat pensil atau hiasan meja",
        "gelas": "dapat dibuat menjadi tempat pensil atau kontainer lain",
        "botol kaca": "dapat dibuat menjadi tempat pensil atau pot bunga",
        "pecahan kaca": "tidak dapat digunakan untuk DIY karena berbahaya, sebaiknya langsung dibuang",
        "kulit buah": "dapat dibuat menjadi kompos atau pupuk organik",
        "sisa sayur": "dapat dibuat menjadi kompos atau pupuk organik",
        "tulang": "dapat dibuat menjadi bubuk kalsium atau pupuk organik",
        "elektronik rusak": "tidak dapat digunakan untuk DIY karena berbahaya, sebaiknya langsung dibuang",
        "baterai": "tidak dapat digunakan untuk DIY karena berbahaya, sebaiknya langsung dibuang",
        "tutup botol besi": "dapat dibuat menjadi gantungan kunci atau hiasan dinding",
        "kaleng": "dapat dibuat menjadi pot bunga atau tempat pensil",
        "paku": "dapat digunakan untuk proyek DIY hiasan, tapi sebaiknya langsung dibuang supaya aman"
    }
    if benda.lower() in data:
        pendapat = data[benda.lower()]
        await ctx.send(f'{benda} {pendapat}.')
    else:
        await ctx.send(f'{benda} tidak ditemukan di database.')

bot.run("Secret Token")
