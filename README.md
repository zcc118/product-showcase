# 拾物日常 · 商品展示 Demo

纯静态 HTML/CSS/JavaScript，无运行时依赖、无构建步骤。8 件样例商品，4 个分类，24 张本地 SVG 排版占位图。占位图不是商品实拍，可离线加载、自由替换。支持响应式卡片、分类与关键词组合筛选、详情弹窗、多图缩略图/方向键浏览、微信信息展示和咨询文案复制。没有后端、数据库、登录、购物车或支付。

## 本地预览

在本目录打开终端，运行：

```sh
python3 preview.py
```

打开 http://127.0.0.1:8765 。如端口占用，运行 `python3 preview.py 8766`。
不要双击 index.html 使用 file:// 打开：浏览器会限制读取 JSON。也可用 VS Code Live Server 打开 public/index.html。Python 服务仅用于本地预览，不参与线上部署。

## Cloudflare Pages 部署

本次仅交付文件，未上传 Cloudflare。

- 直接上传：在 Cloudflare 的 Workers & Pages 中创建 Pages 项目，选择 Direct Upload，上传 **public 文件夹**或交付的 **cloudflare-pages.zip**；确保 index.html 位于上传内容的根目录。按页面提示部署，即可获得 pages.dev 地址。
- Git 集成：将项目提交至仓库，选择静态/无框架，构建命令留空，输出目录为 `public`（如果仓库根目录是本项目的上级，则设置项目根目录为 `product-showcase`）。
- 无需环境变量、数据库、Worker 或 Functions。
- 官方说明：https://developers.cloudflare.com/pages/get-started/direct-upload/
- 静态 HTML：https://developers.cloudflare.com/pages/framework-guides/deploy-anything/

## 目录

```text
product-showcase/
├── README.md
├── DATA_FORMAT.md
├── preview.py             本地静态预览
├── tools/validate.py      数据与图片路径校验
└── public/                只部署此目录
    ├── index.html
    ├── data/
    │   ├── products.json  商品唯一数据源
    │   └── site.json      联系方式
    └── assets/
        ├── app.js
        ├── style.css
        └── images/
            ├── A001/01.svg、02.svg、03.svg
            ├── ...
            └── fallback.svg
```

## 换成真实商品

1. 按 DATA_FORMAT.md 更新 public/data/products.json。
2. 真实照片存入 public/assets/images/商品编号/，推荐 01.webp、02.webp、03.webp。更新 JSON 中 images 数组为对应路径。第一张作为封面，数组顺序就是详情顺序。
3. 修改 public/data/site.json，将 demo 改为 false，wechat 改成真实微信号；可填 email 启用邮件入口，空字符串则隐藏邮件。页面不会自动发送消息。
4. 运行 `python3 tools/validate.py` 校验，预览确认后重新上传 public。

建议图片长边 1200–1600 像素，单张尽量控制在 100–300 KB；主图保持一致比例。照片不要嵌入 Excel，使用商品编号目录对应。此 Demo 不包含 Excel 转换器、图片压缩器或在线上传后台；下次可按固定字段补充离线转换工具。

所有样例价格、材质、描述与微信号均为虚构演示数据。页面店名与介绍在 index.html 中修改，商品与联系方式不需要改页面代码。

## 注意

“下架”只表示在界面不展示，静态 JSON 仍可公开读取。正式发布时应从生成的 JSON 中排除任何不想公开的数据。
支持现代 Chrome、Edge、Safari、Firefox。复制功能在安全上下文可用；浏览器拒绝时会选中咨询文案，提示手动复制。
