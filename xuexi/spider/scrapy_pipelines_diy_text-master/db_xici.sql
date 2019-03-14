/*
Navicat MySQL Data Transfer

Source Server         : db_xici
Source Server Version : 50721
Source Host           : 192.168.0.100:3306
Source Database       : db_xici

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-04-18 17:13:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for xicidaili
-- ----------------------------
DROP TABLE IF EXISTS `xicidaili`;
CREATE TABLE `xicidaili` (
  `id` int(255) unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(1000) NOT NULL,
  `ipaddress` varchar(1000) NOT NULL,
  `port` int(255) NOT NULL,
  `serveraddr` varchar(50) NOT NULL,
  `isanonymous` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `alivetime` varchar(30) NOT NULL,
  `Verifictiontime` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xicidaili
-- ----------------------------
INSERT INTO `xicidaili` VALUES ('4', 'http://fs.xicidaili.com/images/flag/cn.png', '180.160.121.198', '8118', '上海', '高匿', '高匿', '20小时', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('5', 'http://fs.xicidaili.com/images/flag/cn.png', '114.239.124.16', '61234', '江苏宿迁', '高匿', '高匿', '2小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('6', 'http://fs.xicidaili.com/images/flag/cn.png', '60.177.224.47', '18118', '浙江杭州', '高匿', '高匿', '4小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('7', 'http://fs.xicidaili.com/images/flag/cn.png', '61.135.217.7', '80', '北京', '高匿', '高匿', '705天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('8', 'http://fs.xicidaili.com/images/flag/cn.png', '60.166.192.245', '61234', '安徽合肥', '高匿', '高匿', '11小时', '2分钟前');
INSERT INTO `xicidaili` VALUES ('9', 'http://fs.xicidaili.com/images/flag/cn.png', '183.159.90.191', '18118', '浙江杭州', '高匿', '高匿', '3小时', '2分钟前');
INSERT INTO `xicidaili` VALUES ('10', 'http://fs.xicidaili.com/images/flag/cn.png', '113.90.244.255', '8118', '广东深圳', '高匿', '高匿', '20小时', '2分钟前');
INSERT INTO `xicidaili` VALUES ('11', 'http://fs.xicidaili.com/images/flag/cn.png', '60.177.230.40', '18118', '浙江杭州', '高匿', '高匿', '9天', '3分钟前');
INSERT INTO `xicidaili` VALUES ('12', 'http://fs.xicidaili.com/images/flag/cn.png', '27.209.164.31', '61234', '山东滨州', '高匿', '高匿', '15小时', '3分钟前');
INSERT INTO `xicidaili` VALUES ('13', 'http://fs.xicidaili.com/images/flag/cn.png', '121.237.141.81', '18118', '江苏南京', '高匿', '高匿', '5小时', '3分钟前');
INSERT INTO `xicidaili` VALUES ('14', 'http://fs.xicidaili.com/images/flag/cn.png', '203.174.112.13', '3128', '北京', '透明', '透明', '155天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('15', 'http://fs.xicidaili.com/images/flag/cn.png', '61.144.101.135', '9797', '广东广州市白云区', '透明', '透明', '2小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('16', 'http://fs.xicidaili.com/images/flag/cn.png', '101.37.79.125', '3128', '', '透明', '透明', '251天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('17', 'http://fs.xicidaili.com/images/flag/cn.png', '118.212.137.135', '31288', '江西', '透明', '透明', '71天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('18', 'http://fs.xicidaili.com/images/flag/cn.png', '219.245.18.63', '3128', '陕西西安', '透明', '透明', '20天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('19', 'http://fs.xicidaili.com/images/flag/cn.png', '113.12.72.24', '3128', '广西南宁', '透明', '透明', '75天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('20', 'http://fs.xicidaili.com/images/flag/cn.png', '61.188.215.7', '61202', '四川资阳', '透明', '透明', '20小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('21', 'http://fs.xicidaili.com/images/flag/cn.png', '122.72.18.34', '80', '甘肃', '透明', '透明', '215天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('22', 'http://fs.xicidaili.com/images/flag/cn.png', '114.113.126.86', '80', '北京', '透明', '透明', '71天', '2分钟前');
INSERT INTO `xicidaili` VALUES ('23', 'http://fs.xicidaili.com/images/flag/cn.png', '171.88.52.30', '9999', '', '透明', '透明', '22小时', '10分钟前');
INSERT INTO `xicidaili` VALUES ('24', 'http://fs.xicidaili.com/images/flag/cn.png', '124.235.127.208', '8118', '吉林长春', '高匿', '高匿', '19小时', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('25', 'http://fs.xicidaili.com/images/flag/cn.png', '119.28.152.208', '80', '北京', '透明', '透明', '73天', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('26', 'http://fs.xicidaili.com/images/flag/cn.png', '114.215.95.188', '3128', '北京', '透明', '透明', '48天', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('27', 'http://fs.xicidaili.com/images/flag/cn.png', '122.72.18.35', '80', '甘肃', '透明', '透明', '212天', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('28', 'http://fs.xicidaili.com/images/flag/cn.png', '120.0.60.222', '61202', '河北石家庄', '高匿', '高匿', '23小时', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('29', 'http://fs.xicidaili.com/images/flag/cn.png', '122.114.31.177', '808', '河南郑州', '高匿', '高匿', '142天', '不到1分钟');
INSERT INTO `xicidaili` VALUES ('30', 'http://fs.xicidaili.com/images/flag/cn.png', '58.252.6.165', '9000', '广东东莞', '透明', '透明', '899天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('31', 'http://fs.xicidaili.com/images/flag/cn.png', '125.127.148.199', '61234', '浙江台州', '高匿', '高匿', '9小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('32', 'http://fs.xicidaili.com/images/flag/cn.png', '14.120.183.204', '61234', '广东深圳', '高匿', '高匿', '5小时', '3分钟前');
INSERT INTO `xicidaili` VALUES ('33', 'http://fs.xicidaili.com/images/flag/cn.png', '49.79.192.52', '61234', '江苏', '高匿', '高匿', '7小时', '5分钟前');
INSERT INTO `xicidaili` VALUES ('34', 'http://fs.xicidaili.com/images/flag/cn.png', '111.170.104.181', '61234', '贵州贵阳', '高匿', '高匿', '6小时', '6分钟前');
INSERT INTO `xicidaili` VALUES ('35', 'http://fs.xicidaili.com/images/flag/cn.png', '60.177.224.111', '18118', '浙江杭州', '高匿', '高匿', '14小时', '8分钟前');
INSERT INTO `xicidaili` VALUES ('36', 'http://fs.xicidaili.com/images/flag/cn.png', '223.241.119.80', '18118', '安徽', '高匿', '高匿', '12天', '9分钟前');
INSERT INTO `xicidaili` VALUES ('37', 'http://fs.xicidaili.com/images/flag/cn.png', '110.73.30.246', '6666', '广西防城港', '高匿', '高匿', '1920天', '7 天');
INSERT INTO `xicidaili` VALUES ('38', 'http://fs.xicidaili.com/images/flag/cn.png', '121.31.103.33', '6666', '广西防城港', '高匿', '高匿', '1806天', '3 月前');
INSERT INTO `xicidaili` VALUES ('39', 'http://fs.xicidaili.com/images/flag/cn.png', '112.114.76.176', '6668', '云南临沧', '高匿', '高匿', '1808天', '4 月前');
INSERT INTO `xicidaili` VALUES ('40', 'http://fs.xicidaili.com/images/flag/cn.png', '113.121.245.32', '6667', '山东德州', '高匿', '高匿', '1586天', '9 月前');
INSERT INTO `xicidaili` VALUES ('41', 'http://fs.xicidaili.com/images/flag/cn.png', '116.28.106.165', '6666', '广东中山', '高匿', '高匿', '1561天', '10 月前');
INSERT INTO `xicidaili` VALUES ('42', 'http://fs.xicidaili.com/images/flag/cn.png', '110.73.32.7', '6666', '广西防城港', '高匿', '高匿', '1489天', '12 月前');
INSERT INTO `xicidaili` VALUES ('43', 'http://fs.xicidaili.com/images/flag/cn.png', '111.124.231.101', '6668', '贵州铜仁地区铜仁', '高匿', '高匿', '1416天', '1 年前');
INSERT INTO `xicidaili` VALUES ('44', 'http://fs.xicidaili.com/images/flag/cn.png', '113.122.42.161', '6675', '山东菏泽', '高匿', '高匿', '1366天', '1 年前');
INSERT INTO `xicidaili` VALUES ('45', 'http://fs.xicidaili.com/images/flag/cn.png', '110.72.20.245', '6673', '广西贵港', '高匿', '高匿', '1466天', '1 年前');
INSERT INTO `xicidaili` VALUES ('46', 'http://fs.xicidaili.com/images/flag/cn.png', '122.89.138.20', '6675', '江苏徐州', '高匿', '高匿', '1258天', '大约 2 年');
INSERT INTO `xicidaili` VALUES ('47', 'http://fs.xicidaili.com/images/flag/cn.png', '60.177.229.109', '18118', '浙江杭州', '高匿', '高匿', '4小时', '2分钟前');
INSERT INTO `xicidaili` VALUES ('48', 'http://fs.xicidaili.com/images/flag/cn.png', '183.159.84.196', '18118', '浙江杭州', '高匿', '高匿', '1天', '2分钟前');
INSERT INTO `xicidaili` VALUES ('49', 'http://fs.xicidaili.com/images/flag/cn.png', '118.122.92.252', '37901', '四川成都', '高匿', '高匿', '5天', '3分钟前');
INSERT INTO `xicidaili` VALUES ('50', 'http://fs.xicidaili.com/images/flag/cn.png', '39.77.104.193', '8118', '山东', '高匿', '高匿', '15小时', '3分钟前');
INSERT INTO `xicidaili` VALUES ('51', 'http://fs.xicidaili.com/images/flag/cn.png', '114.99.73.111', '61234', '安徽安庆', '高匿', '高匿', '20小时', '3分钟前');
INSERT INTO `xicidaili` VALUES ('52', 'http://fs.xicidaili.com/images/flag/cn.png', '119.127.18.131', '9797', '广东佛山', '透明', '透明', '16小时', '1分钟前');
INSERT INTO `xicidaili` VALUES ('53', 'http://fs.xicidaili.com/images/flag/cn.png', '114.113.126.82', '80', '北京', '透明', '透明', '60天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('54', 'http://fs.xicidaili.com/images/flag/cn.png', '60.190.199.68', '808', '浙江绍兴', '透明', '透明', '1天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('55', 'http://fs.xicidaili.com/images/flag/cn.png', '139.224.80.139', '3128', '', '透明', '透明', '106天', '1分钟前');
INSERT INTO `xicidaili` VALUES ('56', 'http://fs.xicidaili.com/images/flag/cn.png', '120.77.254.116', '3128', '长城宽带', '透明', '透明', '67天', '5分钟前');
INSERT INTO `xicidaili` VALUES ('57', 'http://fs.xicidaili.com/images/flag/cn.png', '14.29.47.90', '3128', '广东', '透明', '透明', '36天', '10分钟前');
INSERT INTO `xicidaili` VALUES ('58', 'http://fs.xicidaili.com/images/flag/cn.png', '116.85.52.186', '8118', '北京', '高匿', '高匿', '2小时', '5分钟前');
INSERT INTO `xicidaili` VALUES ('59', 'http://fs.xicidaili.com/images/flag/cn.png', '183.159.86.211', '18118', '浙江杭州', '高匿', '高匿', '4天', '5分钟前');
INSERT INTO `xicidaili` VALUES ('60', 'http://fs.xicidaili.com/images/flag/cn.png', '223.241.78.47', '8010', '安徽芜湖', '高匿', '高匿', '93天', '8分钟前');
INSERT INTO `xicidaili` VALUES ('61', 'http://fs.xicidaili.com/images/flag/cn.png', '211.147.67.150', '80', '上海', '高匿', '高匿', '88天', '9分钟前');
INSERT INTO `xicidaili` VALUES ('62', 'http://fs.xicidaili.com/images/flag/cn.png', '223.241.117.169', '18118', '安徽', '高匿', '高匿', '8天', '10分钟前');
INSERT INTO `xicidaili` VALUES ('63', 'http://fs.xicidaili.com/images/flag/cn.png', '112.114.78.54', '6673', '云南临沧', '高匿', '高匿', '1813天', '3 月前');
INSERT INTO `xicidaili` VALUES ('64', 'http://fs.xicidaili.com/images/flag/cn.png', '171.38.64.67', '6675', '广西玉林', '高匿', '高匿', '1803天', '3 月前');
INSERT INTO `xicidaili` VALUES ('65', 'http://fs.xicidaili.com/images/flag/cn.png', '222.172.239.69', '6666', '云南昆明市呈贡县', '高匿', '高匿', '1763天', '4 月前');
INSERT INTO `xicidaili` VALUES ('66', 'http://fs.xicidaili.com/images/flag/cn.png', '114.239.253.38', '6666', '江苏宿迁市泗阳县', '高匿', '高匿', '1571天', '10 月前');
INSERT INTO `xicidaili` VALUES ('67', 'http://fs.xicidaili.com/images/flag/cn.png', '220.179.214.77', '6666', '安徽铜陵', '高匿', '高匿', '1556天', '12 月前');
INSERT INTO `xicidaili` VALUES ('68', 'http://fs.xicidaili.com/images/flag/cn.png', '114.139.48.8', '6668', '贵州遵义', '高匿', '高匿', '1458天', '1 年前');
INSERT INTO `xicidaili` VALUES ('69', 'http://fs.xicidaili.com/images/flag/cn.png', '118.80.181.186', '6675', '山西阳泉', '高匿', '高匿', '1476天', '1 年前');
INSERT INTO `xicidaili` VALUES ('70', 'http://fs.xicidaili.com/images/flag/cn.png', '60.211.17.10', '6675', '山东德州', '高匿', '高匿', '1471天', '1 年前');
INSERT INTO `xicidaili` VALUES ('71', 'http://fs.xicidaili.com/images/flag/cn.png', '110.73.33.207', '6673', '广西防城港', '高匿', '高匿', '1415天', '1 年前');
INSERT INTO `xicidaili` VALUES ('72', 'http://fs.xicidaili.com/images/flag/cn.png', '61.138.104.30', '1080', '内蒙古包头', '高匿', '高匿', '1196天', '2 年前');
