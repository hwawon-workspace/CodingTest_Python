-- 코드를 입력하세요
-- 조회수 가장 높은 중고거래 게시물
    -- max view인 게시글 BOARD_ID 찾아서 FROM USED_GOODS_FILE
    -- max(views) FROM USED_GOODS_GOARD
-- 청ㅁ부파일 경로
-- 기본 경로: /home/grep/src/
-- 게시글 id 기준 디렉토리 구분 CONCAT(BOARD_ID, '/')
-- 파일이름: 파이id, 파일이름, 파일확장자로 구성 CONCAT(FILE_ID, FILE_NAME, FILE_EXT)

SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT BOARD_ID
                  FROM (SELECT BOARD_ID, RANK() OVER (ORDER BY VIEWS DESC) AS R
                        FROM USED_GOODS_BOARD) AS BAORD_R 
                  WHERE R = 1)
ORDER BY FILE_ID DESC;