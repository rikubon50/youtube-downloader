import streamlit as st
from PIL import Image
import os
import tempfile
from yt_dlp import YoutubeDL

# --- ロゴ表示 ---
logo = Image.open("Eagles.png")  # ← ファイル名合わせてね
st.image(logo, use_container_width=True)

st.title("📥 YouTube動画ダウンローダー")

url = st.text_input("🎬 ダウンロードしたい動画のURLを入力してください")

if st.button("ダウンロード開始"):
    if url:
        st.info("ダウンロード中... しばらくお待ちください。")
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                # 出力パスを指定（mp4）
                output_path = os.path.join(tmpdir, '%(title)s.%(ext)s')
                ydl_opts = {
                    'format': 'best[ext=mp4]/best',
                    'outtmpl': output_path,
                    'noplaylist': True,
                    'quiet': True,
                }

                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)

                # 動画を読み込んでバイナリデータに変換
                with open(filename, "rb") as f:
                    video_bytes = f.read()

                # ダウンロードボタン表示
                st.success("✅ ダウンロード準備完了！")
                st.download_button(
                    label="📥 動画をダウンロード",
                    data=video_bytes,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"❌ エラーが発生しました: {e}")
    else:
        st.warning("⚠️ URLを入力してください。")
