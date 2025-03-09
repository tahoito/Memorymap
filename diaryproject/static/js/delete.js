document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            const diaryId = this.getAttribute("data-id");
            console.log("削除対象の diaryId:", diaryId);  // ✅ ここで確認！

            if (!diaryId) {
                console.error("エラー: diaryId が取得できません！");
                return;
            }

            if (confirm("本当に削除しますか？")) {
                fetch(`/diary/delete/${diaryId}/ajax_delete/`, {  // ✅ URL をデバッグ
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCsrfToken(),
                        "Content-Type": "application/json"
                    }
                })
                .then(response => response.json())
                .then(data => {
                    console.log("サーバーからのレスポンス:", data);
                    if (data.status === "success") {
                        alert("削除しました！");
                        location.reload();
                    } else {
                        alert("削除に失敗しました！");
                    }
                })
                .catch(error => console.error("エラー:", error));
            }
        });
    });
});


function getCsrfToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}