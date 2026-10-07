# 商品数据约定（v1）

public/data/products.json 根对象包含 schemaVersion: 1 与 products 数组。每件商品字段如下，未来 Excel 一行对应一件商品：

| Excel 列 | JSON 字段 | 规则 |
| --- | --- | --- |
| 商品编号 | id | 必填，唯一；英文字母/数字/短横线/下划线，如 A001；保存为文本 |
| 商品名称 | name | 必填文字 |
| 分类 | category | 必填文字；页面自动生成分类按钮，不使用“全部”作分类名 |
| 价格 | price | 必填，非负数字，最多两位小数；不要带 ¥ 或“元” |
| 币种 | currency | 固定 CNY，当前页面以人民币展示 |
| 描述 | description | 必填纯文本；搜索同时匹配编号、名称、分类、描述 |
| 状态 | status | 上架 / 下架；仅上架显示 |
| 排序 | sort | 非负整数，数字越小越靠前 |
| 标签 | tag | 可选短文字，如“本周精选” |
| 材质 | specs.材质 | 可选文字 |
| 规格 | specs.规格 | 可选文字 |

images 为至少一张图片的路径数组，路径相对于 public 根目录，不以 / 开头。建议未来转换器按照商品编号扫描 `assets/images/A001/`，按文件名排序，生成 images；Excel 不需要手动填写链接。采用 01、02、03 两位编号以确保顺序。

```json
{
  "schemaVersion": 1,
  "products": [{
    "id": "A001",
    "name": "日常帆布托特包",
    "category": "随行包袋",
    "price": 129,
    "currency": "CNY",
    "description": "装下书本、电脑和随行小物。",
    "images": ["assets/images/A001/01.webp", "assets/images/A001/02.webp"],
    "status": "上架",
    "sort": 10,
    "tag": "本周精选",
    "specs": {"材质": "棉帆布", "规格": "38 × 32 × 12 cm"}
  }]
}
```

未来朋友维护的输入包建议为 `商品.xlsx` + `images/商品编号/01.jpg`。转换工具读取 Excel、校验编号与图片、压缩照片，再输出本 Demo 的 JSON 和图片目录。导入应以完整数据包为准，避免旧商品残留；此流程是扩展约定，当前交付没有实现 Excel 导入。

## 联系方式

```json
{
  "contact": {
    "demo": false,
    "wechat": "替换为店主真实微信号",
    "email": "",
    "note": "工作日 10:00–18:00，欢迎咨询。"
  }
}
```

demo=true 时页面明确显示演示提示；不要在未填写真实联系方式时设置为 false。微信是可阅读文本，不承诺通过网页直接唤起微信。咨询按钮会生成含名称和编号的文案，访客复制后自行发送。
