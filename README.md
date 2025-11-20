# 宇宙巡航機 (Space Invader)

這是一個使用 Python 和 Pygame 開發的簡單太空射擊遊戲。玩家控制一艘太空船，必須擊落不斷逼近的敵人艦隊。

## 功能特色

*   **玩家控制**：使用鍵盤左右移動太空船。
*   **射擊機制**：發射子彈消滅敵人。
*   **敵人AI**：敵人會左右移動，並在碰到邊界時下降。
*   **碰撞偵測**：子彈擊中敵人會將其消滅，敵人撞到玩家則遊戲結束。

## 安裝需求

*   Python 3.x
*   Pygame

## 安裝說明

本專案建議使用 [uv](https://github.com/astral-sh/uv) 進行虛擬環境與套件管理。

1.  **安裝 uv** (若尚未安裝):

    ```bash
    # macOS / Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **建立虛擬環境**:

    ```bash
    uv venv --python 3.13 venv01
    ```

3.  **啟動虛擬環境**:

    *   macOS / Linux:
        ```bash
        source venv01/bin/activate
        ```
    *   Windows:
        ```bash
        venv01\Scripts\activate
        ```

4.  **安裝 Pygame**:

    ```bash
    uv pip install pygame
    ```

## 如何執行

在終端機中執行以下指令啟動遊戲：

```bash
python space_invader.py
```

## 遊戲操作

*   **左方向鍵 (←)**：向左移動
*   **右方向鍵 (→)**：向右移動
*   **空白鍵 (Space)**：發射子彈
*   **關閉視窗**：退出遊戲

## 遊戲規則

*   盡可能消滅所有紅色方塊（敵人）。
*   避免敵人觸碰到您的綠色方塊（玩家）。
*   如果敵人撞到玩家，遊戲結束 (Game Over)。

## 授權

此專案僅供教學與練習使用。
