import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

# App page config
st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 10px;
            color: #1f4e79;
        }
        .sub-title {
            text-align: center;
            font-size: 1.3rem;
            color: #444;
            margin-bottom: 40px;
        }
        .section-title {
            font-size: 2rem;
            font-weight: 600;
            margin-top: 30px;
            color: #444;
        }
        .css-1aumxhk {padding-top: 0rem;}
        .st-dh {margin-top: 1.5rem;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("💬 WhatsApp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("📁 Upload your chat file")

# Main title
st.markdown('<div class="main-title">📱 WhatsApp Chat Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Analyze group or personal chats using cool graphs and stats</div>', unsafe_allow_html=True)

# Main content
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.markdown("### 📄 Preview of Chat Data")
    st.dataframe(df)

    # User selection
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("👤 Select user to analyze", user_list)

    if st.sidebar.button("🔍 Show Analysis"):

        # Fetch stats
        num_messages, words, media_len, len_of_links = helper.fetch_stats(selected_user, df)

        # Show KPIs
        st.markdown('<div class="section-title">📈 Key Statistics</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("✉️ Messages", num_messages)
        with col2:
            st.metric("📝 Words", words)
        with col3:
            st.metric("📸 Media Shared", media_len)
        with col4:
            st.metric("🔗 Links Shared", len_of_links)

        # Monthly timeline
        st.markdown('<div class="section-title">📅 Monthly Timeline</div>', unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Daily timeline
        st.markdown('<div class="section-title">📆 Daily Timeline</div>', unsafe_allow_html=True)
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_dates'], daily_timeline['message'], color='black')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Activity Maps
        st.markdown('<div class="section-title">🗓️ Activity Map</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🗓️ Busiest Days")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='#33a1fd')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.subheader("📅 Busiest Months")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color="orange")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Heatmap
        st.markdown('<div class="section-title">🌡️ Weekly Activity Heatmap</div>', unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(user_heatmap, ax=ax, cmap='YlGnBu')
        st.pyplot(fig)

        # Most busy users
        if selected_user == 'Overall':
            st.markdown('<div class="section-title">👥 Most Active Users</div>', unsafe_allow_html=True)
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.markdown('<div class="section-title">☁️ Word Cloud</div>', unsafe_allow_html=True)
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig)

        # Stopwords WordCloud
        st.markdown('<div class="section-title">🔤 Word Cloud (Stopwords)</div>', unsafe_allow_html=True)
        df_wc_some = helper.create_wordcloud_for_some(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc_some)
        ax.axis("off")
        st.pyplot(fig)

        # Most common words
        st.markdown('<div class="section-title">🗣️ Most Common Words</div>', unsafe_allow_html=True)
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(most_common_df[0], most_common_df[1], color='purple')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Emoji Analysis
        st.markdown('<div class="section-title">😊 Emoji Analysis</div>', unsafe_allow_html=True)
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['count'], labels=emoji_df['emoji'], autopct='%1.1f%%', startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
