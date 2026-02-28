from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


# リクエストの受け皿
class QueryRequest(BaseModel):
    query: str


@app.post("/api/query")
def mock_query(request: QueryRequest):
    # 受け取った質問を混ぜて返す
    return {
        "answer": f"「{request.query}」ですね！これはFastAPIからのテスト応答です。",
        "contexts": [
            "使用せずに設\n定した場合と比較して，設定完了までの時間がどの程度\n短縮されたか，といった作業効率の観点からも評価を行\nう．実験結果に基づき提案手法の効果を明らかにする．\n\n\n## 謝辞\n\n本稿をまとめるに当たり，研究設備を貸与いただき研\n究内容に関してご意見をいただいたエンカレッジ・テク\nノロジ株式会社の関係各位に深謝する．\n\n\n## 参考文献\n\n[1] エンカレッジ・テクノロジ株式会社, ” 証跡管理”,https://product.et-x.jp/solution/log\n[2] 竹内 謙仁, 九鬼 琉, 佐々木 貴之, 吉岡 克成, ”LLMを用いたユーザマニュアル解析による機器に即した IoT セキュリティ対策手順の生成”, October 2024,https://ipsj.ixsq.nii.ac.jp/records/240825\n[3] Vectify AI, PageIndex, https://github.com/VectifyAI/PageIndex\n[4] Jacek Czerwonka, ”Pairwise Testing”, https://www.pairwise.org\n[5",
            ". 関連研究\n\n本研究と関連の深い先行研究として，竹内らの「LLM\nを用いたユーザマニュアル解析による機器に即した IoT\nセキュリティ対策手順の生成」がある [2]．竹内らの研究\nでは，IoT 機器のマニュアルを LLM によって解析し，実\n際の機器の設定画面の操作に沿った手順を生成できるか\nを調査した．その結果，97.4% の場合において，マニュ\nアルに記載されている情報に沿った対策手順が生成され\nた．OpenAI の GPT-4o を使用し，プロンプトエンジニ\nアリングを行うことで対策手順を生成させていたことが\n大きな特徴である．\nまた，Vectify AI が開発した PageIndex は現段階では，\nGitHub リポジトリや技術ブログのみで公開されている\n手法ではあるが，ベンチマークで高いスコアを出してい\nる [3]．ベクトルデータベースを用いた従来の RAG は，\nテーマ番号 坂本研-01\n多数のセクションで類似した単語が使われているものの\n重要な詳細が異なるような専門分野では必要な情報を取\n得できない場合がある．上記課題を改善するための技術\nが PageIndex である．PageIndex",
            "た従来の RAG は，\nテーマ番号 坂本研-01\n多数のセクションで類似した単語が使われているものの\n重要な詳細が異なるような専門分野では必要な情報を取\n得できない場合がある．上記課題を改善するための技術\nが PageIndex である．PageIndex は，文書の「目次」ツ\nリー構造インデックスを生成した後，ツリー検索による\n推論ベースの検索を実行する．PageIndex をベースとし\nた Vectify AI の Mafin2.5 というモデルでは，質問応答\nベンチマーク「FinanceBench」において，98.7% の正解\n率を達成した．FinanceBench は金融系ベンチマークであ\nり，専門用語が使われることが多い領域のベンチマーク\nである．したがって，PageIndex は本研究の現状と類似\nしており応用可能な技術である．\n上記の先行研究は，RAG に関連する技術を使用する\n点で，本研究と共通する背景を持つ．\n\n## 4. 提案手法\n\n本研究では，竹内らの研究で使用していたプロンプト\nエンジニアリングと Vectify AI が開発した PageIndex を\n応用する．特に PageInd",
        ],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
