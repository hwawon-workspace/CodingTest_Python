-- 코드를 작성해주세요
-- 더 업그레이드할 수 없는 아이템: 자기가 PARENT_ITEM_ID에 없음

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT DISTINCT PARENT_ITEM_ID
                     FROM ITEM_TREE
                     WHERE PARENT_ITEM_ID IS NOT NULL
                    )
ORDER BY ITEM_ID DESC;