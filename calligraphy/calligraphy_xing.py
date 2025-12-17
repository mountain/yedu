from PIL import Image, ImageDraw, ImageFont
import random

# ================= 配置区 =================
# 输出文件名
OUTPUT_FILE = "cyber_winter.png"

# 字体路径
FONT_PATH = "/Users/mingli/Library/Fonts/FZWangDXCJF.TTF"
SEAL_FONT_PATH = "/Users/mingli/Library/Fonts/FZZJ-MZFU.TTF"

# 1. 标题
TITLE_TEXT = "哀江南賦序"

# 2. 正文
TEXT_CONTENT = """
粵以戊辰之年建亥之月大盜移國金陵瓦解
余乃竄身荒谷公私塗炭華陽奔命有去無歸
中興道消窮於甲戌三日哭於都亭三年囚於別館
天道周星物極不反傅燮之但悲身世無所求生
袁安之每念王室自然流涕昔桓君山之志事
杜元凱之生平竝有著書咸能自序
潘岳之文采始述家風陸機之詞賦先陳世德
信年始二毛即逢喪亂藐是流離至於暮齒
燕歌遠別悲不自勝楚老相逢泣將何及
畏南山之雨忽踐秦庭讓東海之濱遂餐周粟
下亭漂泊高橋羈旅楚歌非取樂之方
魯酒無忘憂之用追為此賦聊以記言
不無危苦之辭惟以悲哀為主
日暮途遠人間何世將軍一去大樹飄零
壯士不還寒風蕭瑟荊璧睨柱受連城而見欺
載書橫階捧珠盤而不定鍾儀君子
入就南冠之囚季孫行人留守西河之館
申包胥之頓地碎之以首蔡威公之淚
盡加之以血釣臺移柳非玉關之可望
華亭鶴唳豈河橋之可聞
孫策以天下為三分眾裁一旅項籍用江東之子弟
人惟八千遂乃分裂山河宰割天下豈有百萬義師
一朝卷甲芟夷斬伐如草木焉江淮無涯岸之阻
亭壁無藩籬之固頭會箕斂者合從締交
鉏耰棘矜者因利乘便
將非江錶王氣終於三百年乎
是知併吞六合不免軹道之災混一車書
無救平陽之禍嗚呼山嶽崩頹既履危亡之運
春秋迭代必有去故之悲
天意人事可以悽愴傷心者矣
況復舟檝路窮星漢非乘槎可上風飈道阻蓬萊
無可到之期窮者欲達其言勞者須歌其事
陸士衡聞而撫掌是所甘心
張平子見而陋之固其宜矣
"""

# 3. 修改后的落款：乙巳(2025) + 仲冬 + 灵境山房
SIGNATURE = "乙巳仲冬漫书于灵境山房 王铎具草"

# 画布设置
CANVAS_WIDTH = 6300
CANVAS_HEIGHT = 2800
BG_COLOR = (245, 240, 225)
TEXT_COLOR = (20, 20, 20)

FONT_SIZE = 110
LINE_SPACING = 160
CHAR_SPACING = 15
START_X = CANVAS_WIDTH - 250
START_Y = 200


# ==========================================

def create_calligraphy():
    image = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        title_font = ImageFont.truetype(FONT_PATH, int(FONT_SIZE * 1.2))
        small_font = ImageFont.truetype(FONT_PATH, int(FONT_SIZE * 0.6))
        seal_font = ImageFont.truetype(SEAL_FONT_PATH, 50)
    except IOError:
        print(f"Error: 找不到字体文件 {FONT_PATH}")
        return

    current_x = START_X
    current_y = START_Y

    # ================= 绘制标题 =================
    title_start_y = START_Y + 50
    for char in TITLE_TEXT:
        offset_x = random.randint(-1, 1)
        offset_y = random.randint(-1, 1)
        draw.text((current_x + offset_x, title_start_y + offset_y), char, font=title_font, fill=TEXT_COLOR)
        title_start_y += int(FONT_SIZE * 1.2) + CHAR_SPACING

    current_x -= int(LINE_SPACING * 1.5)

    # ================= 绘制正文 =================
    clean_content = TEXT_CONTENT.strip().split('\n')
    for line in clean_content:
        current_y = START_Y + random.randint(-30, 30)
        for char in line:
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-2, 2)
            draw.text((current_x + offset_x, current_y + offset_y), char, font=font, fill=TEXT_COLOR)
            current_y += FONT_SIZE + CHAR_SPACING
        current_x -= LINE_SPACING

    # ================= 绘制落款 =================
    sig_x = current_x - 50
    sig_y = START_Y + 600

    for char in SIGNATURE:
        draw.text((sig_x, sig_y), char, font=small_font, fill=(60, 60, 60))
        sig_y += int(FONT_SIZE * 0.6) + 5

    # ================= 绘制印章 (优化版) =================
    # 手动绘制一个更有质感的印章
    seal_size = 110
    seal_x = sig_x - 20
    seal_y = sig_y + 30
    seal_color = (160, 30, 30)  # 更深一点的朱砂红

    # 1. 画边框 (稍微粗一点，带点圆角或不规则更好，这里简化为加粗)
    draw.rectangle([seal_x, seal_y, seal_x + seal_size, seal_y + seal_size], outline=seal_color, width=8)

    # 2. 画印文 "王铎之印" (2x2 排列)
    seal_chars = [("大", 0, 0), ("宗", 0, 1), ("伯", 1, 0), ("印", 1, 1)]
    char_size = 45
    base_cx = seal_x + 10
    base_cy = seal_y + 10

    for char, row, col in seal_chars:
        # 计算每个字的位置
        cx = base_cx + col * (char_size + 0)  # 紧凑
        cy = base_cy + row * (char_size + 0)
        draw.text((cx, cy), char, font=seal_font, fill=seal_color)

    # 可选：再加一个闲章在标题右侧或下方 (起首章)
    # 比如 "云境"
    head_seal_x = START_X + 20
    head_seal_y = START_Y + int(FONT_SIZE * 1.2 * len(TITLE_TEXT)) + 100
    draw.ellipse([head_seal_x, head_seal_y, head_seal_x + 80, head_seal_y + 120], outline=seal_color, width=5)
    draw.text((head_seal_x + 20, head_seal_y + 10), "云", font=seal_font, fill=seal_color)
    draw.text((head_seal_x + 20, head_seal_y + 60), "境", font=seal_font, fill=seal_color)

    image.save(OUTPUT_FILE)
    print(f"成功生成赛博版书法：{OUTPUT_FILE}")


if __name__ == "__main__":
    create_calligraphy()