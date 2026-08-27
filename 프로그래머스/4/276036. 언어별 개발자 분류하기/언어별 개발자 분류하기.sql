-- 코드를 작성해주세요
-- MAX(그룹화된 컬럼 조건문) -> 그룹 내 각 요소에 대한 0/1값 -> 최대: 1 -> True로 작동

SELECT 
    CASE
        WHEN MAX(S.NAME = 'Python') && MAX(S.CATEGORY = 'Front End') THEN 'A'
        WHEN MAX(S.NAME = 'C#') THEN 'B'
        WHEN MAX(S.CATEGORY = 'Front End') THEN 'C'
        ELSE NULL
    END AS GRADE, ID, EMAIL
FROM SKILLCODES S JOIN DEVELOPERS D ON S.CODE & D.SKILL_CODE = S.CODE
GROUP BY ID, EMAIL
HAVING GRADE IS NOT NULL -- SELECT 다음 HAVING 실행
ORDER BY GRADE, ID
;