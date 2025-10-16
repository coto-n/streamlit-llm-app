from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# --- .envファイルを読み込む ---
load_dotenv()

# --- Streamlitアプリのタイトルと説明 ---
st.title("💬 LLMテストアプリ")
st.write("このアプリでは、質問内容と専門家の種類を選んで、AIが回答します。")

# --- LLMモデル設定 ---
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# --- 入力フォーム ---
user_input = st.text_input("質問を入力してください：")

# --- 専門家の種類を選択 ---
expert = st.radio(
    "回答する専門家の種類を選んでください：",
    ("心理の専門家", "スポーツの専門家", "経済の専門家")
)

# --- 送信ボタンで実行 ---
if st.button("送信"):
    # 選択した専門家に応じてシステムメッセージを変更
    if expert == "心理の専門家":
        system_prompt = "You are a psychologist who gives thoughtful and kind answers in Japanese."
    elif expert == "スポーツの専門家":
        system_prompt = "You are a sports expert who explains with practical advice in Japanese."
    elif expert == "経済の専門家":
        system_prompt = "You are an economics expert who provides logical and data-based answers in Japanese."
    else:
        system_prompt = "You are a helpful assistant who answers in Japanese."

    # LangChain用メッセージを作成
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    # LLMに質問を送信
    result = llm(messages)

    # --- 回答を表示 ---
    st.subheader("💡 回答")
    st.write(result.content)
