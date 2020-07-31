# jianshu
**scrapy 爬取简书**
* * *
使用scrapy crawlspider 爬取简书基础信息
* 爬取字段有: 标题（title）、爬取的网址（origin_url）、内容（content）、头像地址（image_urls）、发布日期（ pub_time）、作者（author）
* 存储数据库说明：存储到postgresql中（同步）
* 保存头像图片：利用scrapy自带的图片下载管道，重写下载图片方法，并在settings中设置自定义的下载图片管道

