## 概要
NowTime.pyはタイムゾーンに応じた時間を出力してくれるモジュールです。

## 使い方

### 基本形式
`nowtime.get("{TIMEZONE}", "{FILTER}")`  

### TIMEZONE(CODE)
> UTCを基準としたオフセット順

`GMT` : グリニッジ標準時+0:00  
`UTC` : 国際標準時+0:00  
`ECT` : ヨーロッパ中央時間+1:00  
`EET` : 東ヨーロッパ時間+2:00  
`ART` : (アラブ) エジプト標準時間+2:00  
`EAT` : 東アフリカ時間+3:00  
`MET` : 中東時間+3:30  
`NET` : 近東時間+4:00  
`PLT` : パキスタン・ラホール時間+5:00  
`IST` : インド標準時+5:30  
`BST` : バングラデシュ標準時+6:00  
`VST` : ベトナム標準時+7:00  
`CTT` : 中国台湾時間+8:00  
`JST` : 日本標準時+9:00  
`ACT` : オーストラリア中央時間+9:30  
`AET` : オーストラリア東部時間+10:00  
`SST` : ソロモン諸島標準時+11:00  
`NST` : ニュージーランド標準時+12:00  
`MIT` : ミッドウェー標準時-11:00  
`HST` : ハワイ標準時-10:00  
`AST` : アラスカ標準時-9:00  
`PST` : 太平洋標準時 (米国およびカナダ)-8:00  
`PNT` : フェニックス標準時-7:00  
`MST` : 山地標準時 (米国およびカナダ)-7:00  
`CST` : 中部標準時 (米国およびカナダ)-6:00  
`EST` : 東部標準時 (米国およびカナダ)-5:00  
`IET` : インディアナ東部標準時-5:00  
`PRT` : プエルトリコおよび米領バージン諸島時間-4:00  
`CNT` : カナダ・ニューファウンドランド島時間-3:30  
`AGT` : アルゼンチン標準時-3:00  
`BET` : ブラジル東部時間-3:00  
`CAT` : 中央アフリカ時間-1:00  

### FILTER
`year` : 年(西暦)  
`month` : 月  
`day` : 日  
`hour` : 時  
`minute` : 分  
`second` : 秒  

### 例
```
> Program
import nowtime

nt = nowtime.get
print(nt("JST", "hour"))

> Output  
21 // 現在時刻(UTC)は12時とする。
```

## その他

### エラーの挙動
数値や設定値が正しくない、または対応していない場合`None`を返答します。  

### エラーの文章
`Error: Incorrect filter value.` : {FILTER}に与えられた値が間違っています。  
`Error: Incorrect month value.` : 月に与えられた値が間違っています。  
`Error: Incorrect timezone value.` : タイムゾーンの設定値が間違っています。  
`Error: :urur: value typo.` : うるう年の判定値が間違っています。  
`Error: :offset_which: value typo.` : オフセットの加減算判定値が間違っています。  

## 更新履歴
v0.0.1 初版 2022-06-03
- 不完全な実装
- JSTのみ対応

v0.0.2 改版 2022-06-04
- 不完全な動作検証
- 誤った処理の修正
- 足りなかった処理の追加
- コードの書き直し
- タイムゾーン(コード)一式に対応

v.0.1.0 改版 2022-06-05  
全体的な処理の修正と時空が歪む問題を修正  
- 簡易的な動作検証
- 誤った処理の修正
- Class処理を削除
- 未入力時にエラーを返答
- エラー出力値を`9999`ではなく`None`に変更

## 感謝
タイムゾーン(コード)の情報  
[publib.boulder.ibm.com](https://publib.boulder.ibm.com/tividd/td/TWS/SC32-1274-02/ja_JA/HTML/SRF_mst269.htm)    