import streamlit as st
from PIL import Image
import os
from yt_dlp import YoutubeDL

# --- ロゴ表示 ---
logo = Image.open("Eagles.png")  # ← ファイル名合わせてね
st.image(logo, use_container_width=True)

st.title("YouTube ダウンローダー（高画質）")
url = st.text_input("動画のURLを入力してください")

if st.button("ダウンロード開始"):
    if url:
        st.info("ダウンロード中...")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),  # サーバー内に保存する例
            'noplaylist': True,
            'quiet': False,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("ダウンロード完了！デスクトップを確認してね✅")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("URLを入力してください！")
