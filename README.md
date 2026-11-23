# pairwise-oauth-redirect-pkce

## 领域

安全

## 主题

OAuth 回调校验

## 说明

精确 redirect、PKCE 与 state 一次性。

初始状态下 `security/oauth_redirect_pkce.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
