# Reflection — Lab 19

**Tên:** Trần Gia Khánh - 2A202600293
**Cohort:** A20-K1
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

Trên slice **exact**, BM25 thường mạnh vì query chứa đúng thuật ngữ có trong văn bản. **Paraphrase** thiên về vector vì cần nối câu diễn đạt khác với cùng chủ đề khi không có literal match. **Mixed** là nơi hybrid (RRF) thường thắng nhất: vừa có từ khóa vừa có diễn đạt lệch, nên gộp xếp hạng từ hai retriever ổn định hơn từng mode riêng. Không dùng hybrid khi ngân sách độ trễ/CPU chặt và chỉ cần BM25; khi cần giải thích truy vết từ khóa (tuân thủ, pháp lý); hoặc khi tập quá nhỏ và chi phí embed không xứng đáng—khi đó chỉ BM25 hoặc chỉ vector có thể đủ và đơn giản hơn.

---

## Điều ngạc nhiên nhất khi làm lab này

RRF với rank 1-based thay đổi một bậc là đủ làm hybrid tụt chất lượng; đo P99 sau warm-up mới phản ánh stack thật.

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _<tên đồng đội nếu có>_
