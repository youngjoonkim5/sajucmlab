#!/usr/bin/env python3
"""
Daily SEO Post Generator for sajucmlab
Generates Korean SEO blog posts in Eleventy format with specific writing style.
"""

import os
import sys
import json
import random
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set

PROJECT_ROOT = Path(__file__).parent.parent
POSTS_DIR = PROJECT_ROOT / "src" / "posts"
TOPICS_FILE = PROJECT_ROOT / "scripts" / "topic_pool.json"
USED_TOPICS_FILE = PROJECT_ROOT / "scripts" / "used_topics.json"

# Topic pool organized by category
TOPIC_POOL = {
    "AI_Tools": [
        ("AI 글쓰기 도구 비교: ChatGPT vs Claude vs Gemini 실전 테스트", "AI 글쓰기 도구"),
        ("프롬프트 엔지니어링 실무: 프로덕션에서 쓰는 10가지 패턴", "프롬프트 엔지니어링"),
        ("AI로 콘텐츠 자동화하기: 블로그 글 초안부터 발행까지", "AI 콘텐츠 자동화"),
        ("로컬 LLM 실행 가이드: Ollama로 GPU 없이 모델 돌리기", "로컬 LLM"),
        ("AI 코딩 어시스턴트 비교: Cursor vs Copilot vs Cline", "AI 코딩 도구"),
        ("RAG 시스템 직접 구현하기: 벡터 DB 없이 시작하는 방법", "RAG 구현"),
        ("AI 에이전트 워크플로우: LangGraph로 멀티에이전트 만들기", "AI 에이전트"),
        ("토큰 비용 절감 실전: 프롬프트 압축과 캐싱 전략", "AI 비용 최적화"),
    ],
    "SEO": [
        ("구글 서치 콘솔 실전: 클릭률 2배 올리는 쿼리 분석법", "구글 서치 콘솔"),
        ("키워드 난이도 0-10 직접 계산하기: Ahrefs 없이 하는 법", "키워드 난이도"),
        ("콘텐츠 갭 분석 자동화: 경쟁사 키워드 훔쳐보기 스크립트", "콘텐츠 갭 분석"),
        ("EEAT 점수 높이기: 경험·전문성·권위·신뢰 콘텐츠 체크리스트", "EEAT"),
        ("스키마 마크업 필수 5가지: Article, FAQ, HowTo, Breadcrumb, Organization", "스키마 마크업"),
        ("내부링크 구조 최적화: 토픽 클러스터로 트래픽 3배 늘리기", "내부링크"),
        ("페이지 속도 90점 만들기: Core Web Vitals 실전 튜닝", "페이지 속도"),
        ("구글 인덱싱 요청 자동화: Indexing API로 즉시 색인시키기", "인덱싱 자동화"),
    ],
    "Automation": [
        ("깃허브 액션으로 블로그 자동 발행: 커밋만 하면 배포 완료", "깃허브 액션"),
        ("크론잡 대신 쓰는 서버리스 스케줄러: Cloudflare Workers + Cron Triggers", "서버리스 스케줄러"),
        ("파이썬으로 웹 스크래핑 윤리적으로 하기: robots.txt 준수와 레이트 리밋", "웹 스크래핑"),
        ("데이터 파이프라인 구축: Airflow 대신 Prefect로 시작하기", "데이터 파이프라인"),
        ("알림 자동화: 슬랙·디스코드·이메일로 배포 상태 실시간 받기", "알림 자동화"),
        ("백업 자동화: S3 + Glacier로 데이터 99.999999999% 보존", "자동 백업"),
    ],
    "Eleventy": [
        ("일레븐티로 블로그 만들기: Jekyll·Hugo에서 마이그레이션 후기", "일레븐티 마이그레이션"),
        ("일레븐티 숏코드 만들기: 재사용 가능한 컴포넌트 패턴", "일레븐티 숏코드"),
        ("일레븐티 이미지 최적화: @11ty/eleventy-img로 WebP 자동 변환", "일레븐티 이미지 최적화"),
        ("일레븐티 컬렉션과 필터: 태그·카테고리·연도별 아카이브 자동 생성", "일레븐티 컬렉션"),
        ("일레븐티 빌드 속도 올리기: 증분 빌드와 캐시 전략", "일레븐티 빌드 최적화"),
        ("일레븐티 플러그인 직접 만들기: RSS·Sitemap·JSON Feed 한 번에", "일레븐티 플러그인"),
    ],
    "Netlify": [
        ("넷플리 함수로 API 만들기: 서버리스 백엔드 5분 완성", "넷플리 함수"),
        ("넷플리 엣지 함수: 리다이렉트·헤더·국가별 분기 처리", "넷플리 엣지 함수"),
        ("넷플리 폼 스팸 차단: 허니팟·리캡차·Allowlist 3중 방어", "넷플리 폼 스팸"),
        ("넷플리 빌드 플러그인 작성: 배포 전·후 자동 작업 추가", "넷플리 빌드 플러그인"),
        ("넷플리 분기 배포: Preview·Branch·Production 환경 분리", "넷플리 분기 배포"),
        ("넷플리 대역폭·빌드 시간 절약: 캐시·압축·CDN 설정 최적화", "넷플리 비용 최적화"),
    ],
    "GSC": [
        ("서치 콘솔 API 파이썬 클라이언트: 일일 리포트 자동 이메일", "GSC API"),
        ("스트라이킹 디스턴스 키워드 자동 발굴: 4-20위 페이지 한 번에 올리기", "스트라이킹 디스턴스"),
        ("클릭률 낮은 페이지 진단: 제목·설명·스니펫 A/B 테스트", "CTR 개선"),
        ("색인 커버리지 에러 해결: 크롤링 안 됨·리다이렉트·noindex 정리", "색인 에러 해결"),
        ("모바일 사용성 문제 자동 감지: Viewport·터치 타겟·폰트 크기", "모바일 사용성"),
    ],
    "Content_Operations": [
        ("콘텐츠 캘린더 자동화: Notion + GitHub Actions로 주간 계획 관리", "콘텐츠 캘린더"),
        ("글쓰기 템플릿 시스템: 구조화된 초안으로 작성 속도 3배", "글쓰기 템플릿"),
        ("콘텐츠 성과 대시보드: GA4 + GSC + BigQuery로 한눈에 보기", "콘텐츠 대시보드"),
        ("리퍼비시 전략: 트래픽 떨어진 글 6개월 후 리라이팅으로 살리기", "콘텐츠 리퍼비시"),
        ("다국어 콘텐츠 관리: i18n 라우팅과 hreflang 자동 생성", "다국어 콘텐츠"),
        ("콘텐츠 품질 게이트: AI 휴머니자·전문가 패널·SEO 체크 자동화", "콘텐츠 품질 게이트"),
    ],
}

# Writing style patterns for variation
HOOKS = [
    "대부분 개발자가 놓치는 게 있다.",
    "공식 문서에는 안 나온다.",
    "삽질 3일 만에 알게 된 사실.",
    "한 줄 코드로 해결된다.",
    "돈 안 들이고 하는 방식이다.",
    "대기업도 안 쓰는 무료 도구다.",
    "직접 써보고 놀란 포인트만 적는다.",
    "검색해도 안 나오는 실무 팁이다.",
]

TRANSITIONS = [
    "이유는 단순하다.",
    "핵심은 하나다.",
    "방법은 의외로 쉽다.",
    "차이는 여기에서 갈린다.",
    "실수는 여기서 터진다.",
]

CTA_PATTERNS = [
    "스크립트는 깃허브에 있다. 지금 클론해서 써라.",
    "코드 복사해서 바로 돌려봐라. 5분 걸린다.",
    "설정 파일 하나만 바꿔도 된다. 즉시 적용된다.",
    "내 레포에 예제 다 있다. 포크만 하면 된다.",
    "터미널 한 줄로 끝난다. 복잡한 설정 필요 없다.",
]


def load_used_topics() -> Set[str]:
    """Load previously used topics to avoid duplicates."""
    if USED_TOPICS_FILE.exists():
        try:
            with open(USED_TOPICS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return set(data.get("used_topics", []))
        except Exception:
            pass
    return set()


def save_used_topic(topic: str):
    """Save a topic as used."""
    used = load_used_topics()
    used.add(topic)
    with open(USED_TOPICS_FILE, "w", encoding="utf-8") as f:
        json.dump({"used_topics": list(used)}, f, ensure_ascii=False, indent=2)


def get_available_topics() -> List[tuple]:
    """Get topics that haven't been used yet."""
    used = load_used_topics()
    available = []
    for category, topics in TOPIC_POOL.items():
        for title, keyword in topics:
            if title not in used:
                available.append((category, title, keyword))
    return available


def select_topic() -> tuple:
    """Select a random unused topic."""
    available = get_available_topics()
    if not available:
        # Reset if all used
        if USED_TOPICS_FILE.exists():
            USED_TOPICS_FILE.unlink()
        available = get_available_topics()
    return random.choice(available)


def generate_slug(title: str) -> str:
    """Generate URL-friendly slug from Korean title."""
    # Simple approach: use first few meaningful words + date
    import re
    # Remove special chars, keep Korean, English, numbers
    cleaned = re.sub(r'[^\w\s가-힣]', '', title)
    words = cleaned.split()[:4]
    slug_base = '-'.join(words)
    # Add hash for uniqueness
    hash_suffix = hashlib.md5(title.encode()).hexdigest()[:6]
    return f"{slug_base}-{hash_suffix}"


def generate_content(category: str, title: str, keyword: str) -> str:
    """Generate post content following the specified writing style."""
    
    hook = random.choice(HOOKS)
    transition = random.choice(TRANSITIONS)
    cta = random.choice(CTA_PATTERNS)
    
    # Category-specific content templates
    templates = {
        "AI_Tools": f"""대부분 개발자가 AI 도구 도입할 때 실수하는 게 있다. 유료 플랜부터 결제한다. 무료 티어로도 충분한데.

{hook}

{transition}

직접 테스트해봤다. {keyword} 관련 도구 10개 이상 돌려봤다. 결론부터 말하겠다.

무료로 충분하다. 단, 제대로 써야 한다.

## 1. 도구 선택 기준 세 가지

첫째, 사용량 제한이 넉넉한가. 둘째, API 키 없이 웹에서 바로 되는가. 셋째, 한국어 프롬프트 이해도가 높은가.

이 세 가지만 충족하면 유료 안 써도 된다.

## 2. 실전 테스트 결과

테스트 조건: 같은 프롬프트, 같은 입력, 출력 품질 비교.

결과는 의외였다. 무료 티어 도구가 유료 도구보다 나은 경우도 있었다. 특히 한국어 문맥 이해에서.

## 3. 바로 적용하는 설정

환경 변수 하나만 넣으면 끝난다. 복잡한 래퍼 클래스 필요 없다.

```bash
export AI_TOOL_API_KEY="your-free-key"
```

{cta}""",
        
        "SEO": f"""SEO 한다고 비싼 툴부터 사는 사람 많다. 필요 없다. 구글이 주는 무료 데이터만 잘 써도 상위 10% 들어간다.

{hook}

{transition}

{keyword} 직접 해봤다. 돈 한 푼 안 들이고.

## 1. 구글 서치 콘솔이 주는 것들

클릭수, 노출수, CTR, 평균 순위. 이 네 가지만 봐도 충분하다. 여기에 쿼리별, 페이지별, 국가별, 디바이스별로 쪼개서 본다.

## 2. 자동화 스크립트 한 줄

매일 아침 이메일로 리포트 온다. 크론잡 하나면 된다.

```bash
0 7 * * * python gsc_daily_report.py --email me@domain.com
```

## 3. 액션 아이템 추출 로직

CTR 낮고 노출 높은 쿼리 → 제목·설명 고치기. 순위 4-20위 키워드 → 내부링크·콘텐츠 보강. 색인 안 된 페이지 → 인덱싱 API 쏘기.

{cta}""",
        
        "Automation": f"""자동화한다고 복잡한 도구 깔지 마라. 크론잡, 깃허브 액션, 셸 스크립트만으로 90% 해결된다.

{hook}

{transition}

{keyword} 직접 구현해봤다. 서버 비용 0원.

## 1. 아키텍처: 이벤트 드리븐이 정답

폴링하지 마라. 웹훅 받아라. 깃허브 푸시 → 액션 트리거 → 빌드 → 배포 → 알림. 이 흐름이면 끝난다.

## 2. 실패 대응 전략

리트라이 3번, 백오프 지수적 증가, 슬랙 알림. 이 세 줄이면 99% 커버된다.

```yaml
- uses: actions/retry@v2
  with:
    max_attempts: 3
    backoff: exponential
```

## 3. 모니터링은 단순하게

성공/실패/소요시간 세 가지만 로그 찍어라. 그라파나 필요 없다. 깃허브 액션 로그로 충분하다.

{cta}""",
        
        "Eleventy": f"""정적 사이트 생성기 고민 멈춰라. 일레븐티가 답이다. 자바스크립트만 알면 된다. 리액트·뷰 몰라도 된다.

{hook}

{transition}

{keyword} 실무 적용해봤다. 빌드 시간 10초 안에 끝난다.

## 1. 왜 일레븐티인가

플러그인 생태계가 자바스크립트다. npm 패키지 그대로 쓴다. 설정 파일도 자바스크립트다. 러닝 커브 거의 없다.

## 2. 컬렉션으로 자동화

태그·카테고리·연도 아카이브 자동 생성. 글 쓰면 알아서 페이지 생긴다. 수동 메뉴 관리 필요 없다.

```javascript
eleventyConfig.addCollection("posts", function() {
  return this.getFilteredByGlob("src/posts/*.md").reverse();
});
```

## 3. 이미지 최적화 내장

`@11ty/eleventy-img` 하나면 WebP·AVIF 자동 변환. 반응형 이미지 태그 자동 생성. srcset 직접 안 짜도 된다.

{cta}""",
        
        "Netlify": f"""넷플리 그냥 호스팅 아니다. 서버리스 백엔드다. 함수·엣지·폼·빌드 플러그인까지 다 된다. 무료 티어로.

{hook}

{transition}

{keyword} 프로덕션에서 쓴다. 월 0원.

## 1. 함수 하나면 API 끝

폴더에 파일 하나 넣으면 `/api/이름`으로 바로 된다. 익스프레스 필요 없다. 콜드 스타트 100ms 안쪽.

```javascript
export default async (req) => {
  return new Response(JSON.stringify({ok: true}));
}
```

## 2. 엣지 함수로 리다이렉트

국가별·디바이스별·헤더별 분기. HTML 리라이트도 된다. 미들웨어 없이 된다.

## 3. 빌드 플러그인으로 자동화

배포 전·후 훅 걸어서 사이트맵 생성, 검색 인덱싱, 알림 발송. 한 번 설정하면 영원히.

{cta}""",
        
        "GSC": f"""구글 서치 콘솔 UI로만 보지 마라. API로 뽑아라. 매일 자동 리포트, 알림, 액션 아이템까지 다 뽑힌다.

{hook}

{transition}

{keyword} 파이썬 클라이언트 직접 짰다. 50줄이면 된다.

## 1. 인증 한 번만

OAuth 토큰 저장해두면 만료 전에 자동 갱신. 서비스 계정 쓰면 더 간단하다.

## 2. 핵심 쿼리 4가지

스트라이킹 디스턴스, CTR 낮음, 색인 안 됨, 모바일 이슈. 이걸 매일 뽑아서 액션 리스트로 만든다.

## 3. 인덱싱 API 연동

색인 안 된 URL 자동으로 구글에 제출. 하루 200개까지 무료. 배치로 한 번에 보낸다.

{cta}""",
        
        "Content_Operations": f"""콘텐츠 운영 엑셀로 하지 마라. 노션 + 깃허브 액션이면 끝난다. 작성→리뷰→발행→성과 추적 자동화된다.

{hook}

{transition}

{keyword} 팀 3명 기준 월 50편 발행한다. 사람이 하는 건 글쓰기뿐이다.

## 1. 파이프라인 설계

노션 데이터베이스 → 깃허브 이슈 → PR → 머지 → 빌드 → 배포 → GA4·GSC 수집 → 대시보드 업데이트.

## 2. 품질 게이트 자동화

AI 휴머니자 패턴 체크, SEO 필수 요소 체크, 링크 유효성 체크. PR 열리면 자동 실행. 실패하면 머지 차단.

## 3. 리퍼비시 자동 탐지

트래픽 30% 이상 하락한 글 자동 감지. 6개월 주기로 리라이팅 후보 뽑아준다. 사람이 판단만 하면 된다.

{cta}""",
    }
    
    content = templates.get(category, templates["AI_Tools"])
    
    # Ensure each sentence on its own line
    lines = []
    for line in content.split('\n'):
        line = line.strip()
        if line:
            # Split by sentence endings (Korean)
            import re
            sentences = re.split(r'(?<=[.!?])\s+', line)
            for s in sentences:
                s = s.strip()
                if s:
                    lines.append(s)
        else:
            lines.append("")
    
    # Join and ensure character count (excluding spaces) is 1200-2000
    result = '\n'.join(lines)
    char_count = len(result.replace(' ', '').replace('\n', ''))
    
    # If too short, add more practical details
    if char_count < 1200:
        additional = """

실무에서 바로 쓰는 체크리스트 추가한다.

체크리스트:
- API 키 발급 받았는지
- 환경 변수 설정했는지
- 테스트 실행해봤는지
- 로그 확인했는지
- 알림 채널 연결했는지
- 예외 처리 추가했는지
- 문서 업데이트했는지

이거만 체크하면 장애 90% 예방된다.

다음 글에서는 실제 운영 중 겪은 장애 사례와 대응법을 공유하겠다. 구독하면 알림 온다."""
        result += additional
    
    # Truncate if too long
    if char_count > 2000:
        result = result[:2000]
        # Find last sentence end
        last_period = max(result.rfind('.'), result.rfind('!'), result.rfind('?'))
        if last_period > 1000:
            result = result[:last_period+1]
    
    return result


def generate_post() -> Dict:
    """Generate a complete post with front matter and content."""
    category, title, keyword = select_topic()
    slug = generate_slug(title)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Mark as used
    save_used_topic(title)
    
    content = generate_content(category, title, keyword)
    
    # Build front matter
    front_matter = f"""---
title: "{title}"
description: "{keyword} 실무 가이드. 직접 구현하고 검증한 방법만 공유합니다."
date: {today}
modified: {today}
permalink: "/{slug}/"
tags:
  - {category.replace('_', ' ')}
  - {keyword}
keyword: "{keyword}"
author: "사주천명연구소"
layout: "post.njk"
draft: false
---

"""
    
    full_content = front_matter + content
    
    return {
        "filename": f"{today}-{slug}.md",
        "title": title,
        "keyword": keyword,
        "category": category,
        "content": full_content,
        "slug": slug,
    }


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        post = generate_post()
        print(f"Filename: {post['filename']}")
        print(f"Title: {post['title']}")
        print(f"Keyword: {post['keyword']}")
        print(f"Category: {post['category']}")
        print(f"Slug: {post['slug']}")
        print(f"Char count (no spaces): {len(post['content'].replace(' ', '').replace('\n', ''))}")
        print("\n--- Content Preview ---")
        print(post['content'][:500])
        print("...")
        return
    
    post = generate_post()
    
    # Write post file
    post_path = POSTS_DIR / post['filename']
    with open(post_path, "w", encoding="utf-8") as f:
        f.write(post['content'])
    
    print(f"Generated: {post['filename']}")
    print(f"Title: {post['title']}")
    print(f"Keyword: {post['keyword']}")
    print(f"Path: {post_path}")


if __name__ == "__main__":
    main()