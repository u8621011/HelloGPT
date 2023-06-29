import json
import openai
from collections import defaultdict
import json 


# 產品資訊
products = {
    "TechPro Ultrabook": {
        "name": "TechPro Ultrabook",
        "category": "電腦與筆記型電腦",
        "brand": "TechPro",
        "model_number": "TP-UB100",
        "warranty": "一年",
        "rating": 4.5,
        "features": ["13.3 吋顯示器", "8GB 記憶體", "256GB SSD硬碟", "Intel Core i5 處理器"],
        "description": "一款適合日常使用的輕薄 Ultrabook。",
        "price": 799.99
    },
    "BlueWave 電競筆電": {
        "name": "BlueWave 電競筆電",
        "category": "電腦與筆記型電腦",
        "brand": "BlueWave",
        "model_number": "BW-GL200",
        "warranty": "兩年",
        "rating": 4.7,
        "features": ["15.6 吋顯示器", "16GB 記憶體", "512GB SSD硬碟", "NVIDIA GeForce RTX 3060 顯示卡"],
        "description": "一款高效能的遊戲筆記型電腦，提供沉浸式體驗",
        "price": 1199.99
    },
    "PowerLite 二合一電腦": {
        "name": "PowerLite 二合一電腦",
        "category": "電腦與筆記型電腦",
        "brand": "PowerLite",
        "model_number": "PL-CV300",
        "warranty": "一年",
        "rating": 4.3,
        "features": ["14 吋觸控螢幕", "8GB 記憶體", "256GB SSD硬碟", "360 度螢幕轉軸"],
        "description": "一款具有反應靈敏觸控螢幕的多功能二合一筆記型電腦",
        "price": 699.99
    },
    "TechPro 桌機": {
        "name": "TechPro 桌機",
        "category": "電腦與筆記型電腦",
        "brand": "TechPro",
        "model_number": "TP-DT500",
        "warranty": "一年",
        "rating": 4.4,
        "features": ["Intel Core i7 處理器", "16GB 記憶體", "1TB 硬碟", "NVIDIA GeForce GTX 1660 顯示卡"],
        "description": "一款適合工作和娛樂的強大桌上型電腦。",
        "price": 999.99
    },
    "BlueWave Chromebook": {
        "name": "BlueWave Chromebook",
        "category": "電腦與筆記型電腦",
        "brand": "BlueWave",
        "model_number": "BW-CB100",
        "warranty": "一年",
        "rating": 4.1,
        "features": ["11.6 吋顯示器", "4GB 記憶體", "32GB eMMC 硬碟", "Chrome 作業系統"],
        "description": "一款便捷的Chromebook，適合在網路上瀏覽和處理基本工作。.",
        "price": 249.99
    },
    "SmartX ProPhone": {
        "name": "SmartX ProPhone",
        "category": "手機和配件",
        "brand": "SmartX",
        "model_number": "SX-PP10",
        "warranty": "一年",
        "rating": 4.6,
        "features": ["6.1 吋顯示器", "128GB 儲存空間", "12MP 雙鏡頭", "5G 網路"],
        "description": "一款功能強大並具有先進照相功能的智慧手機",
        "price": 899.99
    },
    "MobiTech 行動盔甲": {
        "name": "MobiTech 行動電源",
        "category": "手機和配件",
        "brand": "MobiTech",
        "model_number": "MT-PC20",
        "warranty": "一年",
        "rating": 4.3,
        "features": ["5000mAh 電池", "無線充電", "與SmartX ProPhone相容"],
        "description": "一款具有內置電池以及堅固外殼可延長您使用時間的行動電源。",
        "price": 59.99
    },
    "SmartX MiniPhone": {
        "name": "SmartX MiniPhone",
        "category": "手機和配件",
        "brand": "SmartX",
        "model_number": "SX-MP5",
        "warranty": "一年",
        "rating": 4.2,
        "features": ["4.7 吋顯示器", "64GB 儲存空間", "8MP 鏡頭", "4G 網路"],
        "description": "一款小巧且實惠的智慧手機，適合基本任務使用。",
        "price": 399.99
    },
    "MobiTech 無線充電器": {
        "name": "MobiTech 無線充電器",
        "category": "手機和配件",
        "brand": "MobiTech",
        "model_number": "MT-WC10",
        "warranty": "一年",
        "rating": 4.5,
        "features": ["10W 快速充電", "與Qi充電標準相容", "LED 指示燈", "精巧設計"],
        "description": "一款方便的無線充電器，讓您的工作區域無雜亂的電線。",
        "price": 29.99
    },
    "SmartX 耳機": {
        "name": "SmartX 耳機",
        "category": "手機和配件",
        "brand": "SmartX",
        "model_number": "SX-EB20",
        "warranty": "一年",
        "rating": 4.4,
        "features": ["真無線", "藍牙  5.0", "觸控控制", "24 小時播放時間"],
        "description": "一款輕便且音質出色的無線耳機，讓您隨時隨地都能享受音樂。",
        "price": 99.99
    },

    "CineView 4K 液晶電視": {
        "name": "CineView 4K 液晶電視",
        "category": "電視和家庭劇院系統",
        "brand": "CineView",
        "model_number": "CV-4K55",
        "warranty": "兩年",
        "rating": 4.8,
        "features": ["55 吋顯示器", "4K 解析度", "HDR", "智慧電視"],
        "description": "一部色彩鮮豔，並擁有智能功能的令人驚嘆的 4K 電視。",
        "price": 599.99
    },
    "SoundMax 家庭劇院": {
        "name": "SoundMax 家庭劇院",
        "category": "電視和家庭劇院系統",
        "brand": "SoundMax",
        "model_number": "SM-HT100",
        "warranty": "一年",
        "rating": 4.4,
        "features": ["5.1 聲道", "1000W 輸出", "無線重低音", "藍牙"],
        "description": "一部強大的家庭劇院系統，為您提供身臨其境的音效體驗。",
        "price": 399.99
    },
    "CineView 8K 液晶電視": {
        "name": "CineView 8K 液晶電視",
        "category": "電視和家庭劇院系統",
        "brand": "CineView",
        "model_number": "CV-8K65",
        "warranty": "兩年",
        "rating": 4.9,
        "features": ["65 吋顯示器", "8K 解析度", "HDR", "智慧電視"],
        "description": "用這部令人驚嘆的 8K 電視體驗電視工藝的未來。",
        "price": 2999.99
    },
    "SoundMax 音箱": {
        "name": "SoundMax 音箱",
        "category": "電視和家庭劇院系統",
        "brand": "SoundMax",
        "model_number": "SM-SB50",
        "warranty": "一年",
        "rating": 4.3,
        "features": ["2.1 聲道", "300W 輸出", "無線重低音", "藍牙"],
        "description": "使用這款時尚且音質出色的音響升級您的電視聲光效果。",
        "price": 199.99
    },
    "CineView OLED 電視": {
        "name": "CineView OLED 電視",
        "category": "電視和家庭劇院系統",
        "brand": "CineView",
        "model_number": "CV-OLED55",
        "warranty": "兩年",
        "rating": 4.7,
        "features": ["55 吋顯示器", "4K 解析度", "HDR", "智慧電視"],
        "description": "這款 OLED 電視讓您體驗什麼是真正的黑色以及色彩。",
        "price": 1499.99
    },

    "GameSphere X": {
        "name": "GameSphere X",
        "category": "遊戲機和配件",
        "brand": "GameSphere",
        "model_number": "GS-X",
        "warranty": "一年",
        "rating": 4.9,
        "features": ["4K 遊戲", "1TB 儲存空間", "向後相容", "線上多人遊戲"],
        "description": "下一代遊戲機，為您提供最終極的遊戲體驗。",
        "price": 499.99
    },
    "ProGamer 搖桿": {
        "name": "ProGamer 搖桿",
        "category": "遊戲機和配件",
        "brand": "ProGamer",
        "model_number": "PG-C100",
        "warranty": "一年",
        "rating": 4.2,
        "features": ["人體工學設計", "可自訂按鈕", "無線", "可充電電池"],
        "description": "高品質的遊戲控制器，為您提供精準與舒適的操作。",
        "price": 59.99
    },
    "GameSphere Y": {
        "name": "GameSphere Y",
        "category": "遊戲機和配件",
        "brand": "GameSphere",
        "model_number": "GS-Y",
        "warranty": "一年",
        "rating": 4.8,
        "features": ["4K 遊戲", "500GB 儲存空間", "向後相容", "線上多人遊戲"],
        "description": "一台體積精巧、性能強大的遊戲機。",
        "price": 399.99
    },
    "ProGamer 賽車方向盤": {
        "name": "ProGamer R方向盤",
        "category": "遊戲機和配件",
        "brand": "ProGamer",
        "model_number": "PG-RW200",
        "warranty": "一年",
        "rating": 4.5,
        "features": ["動力反饋", "可調踏板", "撥片換檔", "與 GameSphere X 相容"],
        "description": "使用這款逼真的賽車方向盤，提升您的賽車遊戲體驗。",
        "price": 249.99
    },
    "GameSphere VR 頭盔": {
        "name": "GameSphere VR 頭盔",
        "category": "遊戲機和配件",
        "brand": "GameSphere",
        "model_number": "GS-VR",
        "warranty": "一年",
        "rating": 4.6,
        "features": ["沉浸式虛擬實景體驗", "內建耳機", "可調節頭帶", "與 GameSphere X 兼容"],
        "description": "用這款舒適的 VR 頭盔步入虛擬實境的世界。",
        "price": 299.99
    },

    "AudioPhonic 降噪耳機": {
        "name": "AudioPhonic 降噪耳機",
        "category": "音響設備",
        "brand": "AudioPhonic",
        "model_number": "AP-NC100",
        "warranty": "一年",
        "rating": 4.6,
        "features": ["主動降噪", "藍牙", "20 小時電池壽命", "舒適貼合"],
        "description": "使用這款降噪耳機體驗沉浸式的音效。",
        "price": 199.99
    },
    "WaveSound 藍牙喇叭": {
        "name": "WaveSound 藍牙喇叭",
        "category": "音響設備",
        "brand": "WaveSound",
        "model_number": "WS-BS50",
        "warranty": "一年",
        "rating": 4.5,
        "features": ["攜帶式", "10 小時電池壽命", "防水", "內建麥克風"],
        "description": "這款精巧且多功能的藍牙揚聲器適合隨身攜帶。",
        "price": 49.99
    },
    "AudioPhonic 真無線耳機": {
        "name": "AudioPhonic 真無線耳機",
        "category": "音響設備",
        "brand": "AudioPhonic",
        "model_number": "AP-TW20",
        "warranty": "一年",
        "rating": 4.4,
        "features": ["真無線", "藍牙  5.0", "觸控控制", "18 小時電池壽命"],
        "description": "這款舒適的真無線耳機讓您無線享受音樂。",
        "price": 79.99
    },
    "WaveSound 音箱": {
        "name": "WaveSound 音箱",
        "category": "音響設備",
        "brand": "WaveSound",
        "model_number": "WS-SB40",
        "warranty": "一年",
        "rating": 4.3,
        "features": ["2.0 聲道", "80W 輸出", "藍牙", "可掛牆"],
        "description": "使用這款纖薄而強大的音箱升級您的電視音效。",
        "price": 99.99
    },
    "AudioPhonic 黑膠唱盤機": {
        "name": "AudioPhonic 黑膠唱盤機",
        "category": "音響設備",
        "brand": "AudioPhonic",
        "model_number": "AP-TT10",
        "warranty": "一年",
        "rating": 4.2,
        "features": ["3段變速", "內建揚聲器", "藍牙", "USB 錄音"],
        "description": "使用這款現代化的黑膠唱盤機重新發現您的黑膠唱片。",
        "price": 149.99
    },

    "FotoSnap 單眼相機": {
        "name": "FotoSnap 單眼相機",
        "category": "相機和攝影機",
        "brand": "FotoSnap",
        "model_number": "FS-DSLR200",
        "warranty": "一年",
        "rating": 4.7,
        "features": ["24.2MP 感光元件", "1080p 影片", "3 吋 LCD", "可更換鏡頭"],
        "description": "使用這款多功能的單眼相機捕捉精彩照片和視頻。",
        "price": 599.99
    },
    "ActionCam 4K": {
        "name": "ActionCam 4K",
        "category": "相機和攝影機",
        "brand": "ActionCam",
        "model_number": "AC-4K",
        "warranty": "一年",
        "rating": 4.4,
        "features": ["4K 影片", "防水", "影像穩定技術", "Wi-Fi"],
        "description": "使用這款堅固且精巧的 4K 動作攝影機記錄您的冒險。",
        "price": 299.99
    },
    "FotoSnap 無反光鏡相機": {
        "name": "FotoSnap 無反光鏡相機",
        "category": "相機和攝影機",
        "brand": "FotoSnap",
        "model_number": "FS-ML100",
        "warranty": "一年",
        "rating": 4.6,
        "features": ["20.1MP 感光元件", "4K 影片", "3 吋觸控螢幕", "可更換鏡頭"],
        "description": "這款具有先進功能的精巧輕量級無反光鏡相機。",
        "price": 799.99
    },
    "ZoomMaster 攝影機": {
        "name": "ZoomMaster 攝影機",
        "category": "相機和攝影機",
        "brand": "ZoomMaster",
        "model_number": "ZM-CM50",
        "warranty": "一年",
        "rating": 4.3,
        "features": ["1080p 影片", "30x 光學變焦", "3 吋LCD", "影像穩定技術"],
        "description": "用這款易於使用的攝影機捕捉生活的時刻。",
        "price": 249.99
    },
    "FotoSnap 拍立得相機": {
        "name": "FotoSnap 拍立得相機",
        "category": "相機和攝影機",
        "brand": "FotoSnap",
        "model_number": "FS-IC10",
        "warranty": "一年",
        "rating": 4.1,
        "features": ["立即列印", "內建閃光燈", "自拍鏡", "可攜式電池"],
        "description": "用這款有趣和便攜的拍立得相機創造即時回憶。",
        "price": 69.99
    }
}

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def get_products_and_category():
    """
    Used in L5
    """
    products_by_category = defaultdict(list)
    for product_name, product_info in products.items():
        category = product_info.get('category')
        if category:
            products_by_category[category].append(product_info.get('name'))
    
    return dict(products_by_category)

def get_product_by_name(name):
    """
    從產品資料庫內取得特定名稱的產品
    """
    return products.get(name, None)

def get_products_by_category(category):
    """
    從產品資料庫內取得特定類別的產品
    """
    return [product for product in products.values() if product["category"] == category]

def read_string_to_list(input_string):
    """
    將 LLM 的回應轉為 JSON object
    """
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # 單引號改為雙引號，這樣才是合法的 JSON 格式
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None  
    
def generate_output_string(data_list):
    """
    從 LLM 的回應來取得產品資料庫內的 產品以及類別詳細資料
    """
    output_string = ""

    if data_list is None:
        return output_string

    for data in data_list:
        try:
            # 如果有 "products" 屬性，就代表是要查詢產品
            if "products" in data:
                products_list = data["products"]
                for product_name in products_list:
                    # 透過產品名稱取得產品資訊
                    product = get_product_by_name(product_name)
                    if product:
                        # 將產品資訊轉換為 JSON 格式，並加入換行符號
                        output_string += json.dumps(product, indent=4, ensure_ascii=False) + "\n"
                    else:
                        print(f"Error: Product '{product_name}' not found")
            # 如果有 "category" 屬性，就代表是要查詢類別
            elif "category" in data:
                category_name = data["category"]
                # 透過類別名稱取得產品資訊
                category_products = get_products_by_category(category_name)
                for product in category_products:
                    # 將產品資訊轉換為 JSON 格式，並加入換行符號
                    output_string += json.dumps(product, indent=4, ensure_ascii=False) + "\n"
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e}")

    return output_string 

def find_category_and_product(user_input,products_and_category):
    delimiter = "####"
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with {delimiter} characters.
    Output a python list of json objects, where each object has the following format:
        'category': <one of Computers and Laptops, Smartphones and Accessories, Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, Audio Equipment, Cameras and Camcorders>,
    OR
        'products': <a list of products that must be found in the allowed products below>

    Where the categories and products must be found in the customer service query.
    If a product is mentioned, it must be associated with the correct category in the allowed products list below.
    If no products or categories are found, output an empty list.

    The allowed products are provided in JSON format.
    The keys of each item represent the category.
    The values of each item is a list of products that are within that category.
    Allowed products: {products_and_category}
    
    """
    messages =  [  
    {'role':'system', 'content': system_message},    
    {'role':'user', 'content': f"{delimiter}{user_input}{delimiter}"},  
    ] 
    return get_completion_from_messages(messages)


def find_category_and_product_only(user_input,products_and_category):
    delimiter = "####"
    system_message = f"""
    1. 你將會收到一些客戶服務查詢。客戶服務查詢將由 {delimiter} 字元作為分隔符。
    2. 如果客戶訊息中的產品在下方允許產品清單中，你就輸出一個Python物件列表，每個物件同時具有以下格式：
    'category': <以下其中一項：電腦和筆記本，手機和配件，電視和家庭劇院系統，遊戲機和配件，音響設備，相機和攝影機>
    或
    'products': <必須在以下列出的允許產品中找到的產品列表>
    3. 客戶提到下方允許產品清單中的產品時，也同時在在物件屬性列出它對應的類別。
    4. 如果客戶沒有特別提到什麼產品，你只要列出類別就好。
    5. 如果客戶訊息中的產品不在下方允許產品清單中，你就輸出一個空列表。
    6. 如果產品屬性是空的，也不要輸出類別屬性，直接輸出空列表。


    允許的產品：

    手機和配件類別：
    SmartX ProPhone
    MobiTech 行動盔甲
    SmartX MiniPhone
    MobiTech 無線充電器
    SmartX 耳機

    電視和家庭劇院系統類別：
    CineView 4K 液晶電視
    SoundMax 家庭劇院
    CineView 8K 液晶電視
    SoundMax 音箱
    CineView OLED 電視

    相機和攝影機類別：
    FotoSnap 單眼相機
    ActionCam 4K 攝影機
    FotoSnap 無反光鏡相機
    ZoomMaster 攝影機
    FotoSnap 拍立得相機


    你只可以輸出Python物件列表，不能輸出其他任何資訊。
    """
    messages =  [  
    {'role':'system', 'content': system_message},    
    {'role':'user', 'content': f"{delimiter}{user_input}{delimiter}"},  
    ] 
    return get_completion_from_messages(messages)