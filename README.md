## 概要
NowTime.pyはタイムゾーンに応じた時間を出力してくれるものです。

## 使い方

### 基本形式
nowtime.{TYPE}({TIMEZONE}, {FILTER})

### TYPE
`get`:現在時刻の取得  

### TIMEZONE
JST = 日本標準時  

### FILTER
`year`:年(西暦)  
`month`:月  
`day`:日  
`hour`:時  
`minute`:分  
`second`:秒  

### 例
```
> Program
import nowtime

nowtime = nowtime.get("jst", "hour")
print(nowtime)

> Output  
21 // 現在時刻(UTC)は12時とする。  
```

## その他

### エラーの挙動
数値や設定値が正しくない、または対応していない場合`int`型で`9999`を返答します。  

## 更新履歴
v0.0.1 初版 2022-06-03  
JSTのみに対応。多分うごく  

## 実装予定
### 他のタイムゾーンと地域の入力に対応
GMTやJSTみたいな形式とAsia/Tokyoみたいな形式どっちにも対応したい。  

なんか作ってるとき同じようなものを見つけてしまい何とも言えない気分になった。