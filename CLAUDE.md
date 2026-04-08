# Gmail Inbox Zero - הוראות לאייגנט

## כלל עליון
**לפני כל שינוי** - בצע Audit וקבל אישור מהמשתמש. לעולם אל תמחק תווית, פילטר, או מייל ללא אישור מפורש.

---

## פקודות מהירות

### `/audit` - בדיקת מצב נוכחי
1. הרץ `gmail_list_labels` - הצג את כל התוויות הקיימות
2. חפש את כל הפילטרים הקיימים
3. הצג טבלה: קיים / חסר / מיותר לפי המבנה הרצוי
4. **המתן לאישור** לפני כל שינוי

### `/setup` - הגדרה ראשונית (חד-פעמי)
1. הרץ `/audit` קודם
2. צור תוויות חסרות לפי המבנה
3. צור פילטרים חסרים לפי הטבלה
4. **בכל שלב - בקש אישור**

### `/daily-sweep` - ניקיון יומי של הזמנות
1. סרוק תווית `Orders/Products`:
   - ארכב מיילים עם מילות: "delivered", "נמסר", "הגיע", "נאסף", "delivered successfully"
   - שמור מיילים עם: "shipped", "נשלח", "בדרך", "out for delivery", "tracking"
2. סרוק תווית `Orders/Travel`:
   - ארכב הזמנות שתאריך הצ'ק-אין / האירוע **עבר** (לפי היום: {TODAY})
   - שמור הזמנות עם תאריך **עתידי**
3. דווח: כמה מיילים עובדו / ארוכבו / נשארו

### `/clean-promotions` - מחיקת פרסומות ישנות
- מחק מיילים בתווית `Lists/Promotions` ישנים מ-14 יום
- **בקש אישור לפני** ביצוע

### `/archive-old` - ארכוב מיילים ישנים
- ארכב כל מה שישן מ-90 יום מה-Inbox
- **חריגים:** מיילים עם תווית `_Action`, `_Waiting`, או `Orders/*` פעיל
- **בקש אישור לפני** ביצוע

---

## מבנה התוויות הרצוי

```
_Action               ← דורש פעולה ממני - לא דולג על inbox
_Waiting              ← מחכה לתגובה - לא דולג על inbox

Finance/
  Bank                ← בנק (עדכוני חשבון, העברות)
  Salary              ← תלושי שכר
  Investments         ← השקעות ופנסיה
  Insurance           ← ביטוח ובריאות

Orders/
  Products            ← הזמנות מוצרים - Smart Cleanup יומי
  Travel              ← מלונות, טיסות, כרטיסים - Smart Cleanup יומי

Lists/
  Newsletters         ← ניוזלטרים - skip inbox
  Promotions          ← פרסומות - skip inbox, delete after 14d
  Notifications       ← התראות שירותים - skip inbox
```

---

## פילטרים לבניה

| קטגוריה | Query לדוגמה (להתאים לפי audit!) | פעולה |
|---------|----------------------------------|--------|
| Finance/Bank | `from:(*leumi* OR *hapoalim* OR *discount* OR *mizrahi* OR *yahav*)` | Label + Skip Inbox |
| Finance/Insurance | `from:(*clalit* OR *maccabi* OR *meuhedet* OR *menora* OR *harel* OR *migdal*)` | Label + Skip Inbox |
| Finance/Investments | `from:(*psagot* OR *altshuler* OR *IBI* OR *meitav*)` | Label + Skip Inbox |
| Orders/Products | `from:(*amazon* OR *ebay* OR *aliexpress* OR *zara* OR *terminalX*)` | Label + Skip Inbox |
| Orders/Travel | `from:(*booking* OR *airbnb* OR *elal* OR *ryanair* OR *wizzair* OR *issta*)` | Label + Skip Inbox |
| Lists/Newsletters | `unsubscribe OR list-unsubscribe` | Label + Skip Inbox |
| Lists/Promotions | `category:promotions` | Label + Skip Inbox |
| Lists/Notifications | `category:social OR category:updates OR category:forums` | Label + Skip Inbox |

> **חשוב:** ה-queries הם נקודת התחלה. לאחר audit, התאם לפי השולחים האמיתיים שמופיעים בתיבה.

---

## כלל יומי - Inbox Zero

**Inbox = רק מיילים שדורשים תשומת לב היום**

כלל 4D לכל מייל ב-Inbox:
- **Do** - עשה עכשיו (פחות מ-2 דק')
- **Delegate** - העבר למישהו
- **Defer** - דחה → העבר לתווית `_Action`
- **Delete/Archive** - לא רלוונטי → מחק/ארכב

**מטרה:** inbox ריק בסוף כל יום.

---

## הוראות כלליות לאייגנט

1. **תמיד** התחל עם audit לפני שינויים
2. **תמיד** הצג מה עומד לקרות לפני ביצוע
3. בצע פעולות בבאצ'ים קטנים (10-20 מיילים בכל פעם) כדי למנוע שגיאות
4. אם יש ספק לגבי מייל - שמור אותו, אל תמחק
5. דווח תמיד על מה שבוצע: כמה מיילים, אילו פעולות
