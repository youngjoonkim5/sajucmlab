const siteUrl = "https://sajucmlab.com";
const companyUrl = "https://sajucm.com";

const business = {
  koName: "사주천명연구소",
  hanjaName: "四柱天命硏究所",
  businessNumber: "447-86-03952",
  telephone: "+82-070-8095-7405",
  email: "contact@sajucm.com",
  address: {
    country: "KR",
    region: "서울특별시",
    locality: "서초구",
    street: "강남대로 37길 56-31",
    full: "서울특별시 서초구 강남대로 37길 56-31"
  }
};

const locales = {
  ko: {
    lang: "ko",
    path: "/",
    locale: "ko_KR",
    label: "한국어",
    title: "사주천명연구소 | 사주명리 데이터 연구와 상담 인사이트",
    description: "사주천명연구소는 전통 사주명리 해석을 데이터, 콘텐츠, 상담 경험으로 연결하는 리서치 기반 명리 플랫폼입니다.",
    eyebrow: "SajuCM Lab",
    heroTitle: "사주명리의 언어를 더 정확하고 쓸모 있게 연구합니다.",
    heroCopy: "사주천명연구소는 개인의 생년월일시 해석에 머무르지 않고, 명리 지식을 콘텐츠, 데이터, 상담 흐름으로 정리해 누구나 이해할 수 있는 실용적 인사이트로 전환합니다.",
    primaryCta: "문의하기",
    secondaryCta: "회사 사이트 보기",
    blogLabel: "블로그",
    nav: ["연구", "서비스", "FAQ", "문의"],
    stats: [
      ["명리 콘텐츠", "검색 친화적인 해석 자료"],
      ["상담 인사이트", "질문 중심의 풀이 구조"],
      ["데이터 정리", "반복 가능한 명리 지식 체계"]
    ],
    sections: {
      researchTitle: "연구하는 명리",
      researchCopy: "전통 명리의 개념을 현대 독자가 이해할 수 있도록 구조화하고, 실제 상담에서 반복되는 질문을 바탕으로 콘텐츠와 분석 체계를 다듬습니다.",
      servicesTitle: "무엇을 만드나요",
      services: [
        ["사주명리 콘텐츠", "운세, 궁합, 적성, 사업운 등 주요 주제를 검색과 학습에 적합한 글로 정리합니다."],
        ["상담 UX 설계", "사용자가 자신의 질문을 더 명확히 이해하도록 상담 전후의 흐름을 설계합니다."],
        ["데이터 기반 연구", "명리 용어와 해석 패턴을 축적해 일관된 풀이 기준을 만드는 연구를 진행합니다."]
      ],
      proofTitle: "전통과 기술 사이의 균형",
      proofCopy: "사주천명연구소는 과장된 예언보다 맥락 있는 해석을 지향합니다. 생년월일시라는 오래된 입력값을 삶의 선택과 자기이해에 도움이 되는 언어로 번역합니다.",
      faqTitle: "자주 묻는 질문"
    },
    faqs: [
      ["사주천명연구소는 어떤 곳인가요?", "전통 사주명리 지식을 연구하고, 상담과 콘텐츠로 연결하는 명리 전문 연구소입니다."],
      ["온라인으로도 문의할 수 있나요?", "네. 이메일 contact@sajucm.com 또는 대표전화 +82-070-8095-7405로 문의할 수 있습니다."],
      ["sajucmlab.com은 어떤 사이트인가요?", "사주CM의 연구, 콘텐츠, 데이터 기반 명리 인사이트를 소개하는 랜딩 사이트입니다."]
    ]
  },
  ja: {
    lang: "ja",
    path: "/ja/",
    locale: "ja_JP",
    label: "日本語",
    title: "四柱天命研究所 | 四柱推命の研究と相談インサイト",
    description: "四柱天命研究所は、伝統的な四柱推命の解釈をデータ、コンテンツ、相談体験へつなげる研究型プラットフォームです。",
    eyebrow: "SajuCM Lab",
    heroTitle: "四柱推命の言葉を、より正確で実用的な知識へ。",
    heroCopy: "四柱天命研究所は、生年月日時の解釈にとどまらず、命理の知識をコンテンツ、データ、相談の流れとして整理し、理解しやすい洞察へ変換します。",
    primaryCta: "お問い合わせ",
    secondaryCta: "会社サイト",
    blogLabel: "ブログ",
    nav: ["研究", "サービス", "FAQ", "連絡先"],
    stats: [
      ["命理コンテンツ", "検索と学習に適した解説"],
      ["相談インサイト", "質問中心の解釈設計"],
      ["データ整理", "再現性のある知識体系"]
    ],
    sections: {
      researchTitle: "研究する命理",
      researchCopy: "伝統的な命理概念を現代の読者にも理解しやすく構造化し、実際の相談で繰り返される質問をもとに分析体系を磨きます。",
      servicesTitle: "提供する価値",
      services: [
        ["四柱推命コンテンツ", "運勢、相性、適性、事業運などのテーマを読みやすい記事として整理します。"],
        ["相談UX設計", "利用者が自分の問いをより明確に理解できる相談体験を設計します。"],
        ["データ基盤研究", "命理用語と解釈パターンを蓄積し、一貫した判断基準を整えます。"]
      ],
      proofTitle: "伝統と技術のバランス",
      proofCopy: "四柱天命研究所は、過度な予言ではなく文脈のある解釈を大切にします。古くからの入力値を、自己理解と選択に役立つ言葉へ翻訳します。",
      faqTitle: "よくある質問"
    },
    faqs: [
      ["四柱天命研究所とは何ですか？", "伝統的な四柱推命を研究し、相談とコンテンツにつなげる専門研究所です。"],
      ["海外から問い合わせできますか？", "はい。contact@sajucm.com または +82-070-8095-7405 までお問い合わせください。"],
      ["sajucmlab.comは何のサイトですか？", "SajuCMの研究、コンテンツ、データに基づく命理インサイトを紹介するサイトです。"]
    ]
  },
  zh: {
    lang: "zh",
    path: "/zh/",
    locale: "zh_CN",
    label: "中文",
    title: "四柱天命研究所 | 四柱命理研究与咨询洞察",
    description: "四柱天命研究所将传统四柱命理解读连接到数据、内容与咨询体验，打造研究型命理平台。",
    eyebrow: "SajuCM Lab",
    heroTitle: "让四柱命理的语言更准确，也更有用。",
    heroCopy: "四柱天命研究所不止停留在出生年月日时的解释，而是把命理知识整理为内容、数据和咨询流程，转化为更容易理解的实用洞察。",
    primaryCta: "联系我们",
    secondaryCta: "公司网站",
    blogLabel: "博客",
    nav: ["研究", "服务", "FAQ", "联系"],
    stats: [
      ["命理内容", "适合搜索与学习的解读"],
      ["咨询洞察", "以问题为中心的分析结构"],
      ["数据整理", "可持续积累的知识体系"]
    ],
    sections: {
      researchTitle: "研究型命理",
      researchCopy: "我们将传统命理概念结构化，让现代读者更容易理解，并基于真实咨询中反复出现的问题持续完善内容与分析体系。",
      servicesTitle: "我们提供什么",
      services: [
        ["四柱命理内容", "整理运势、合婚、职业倾向、事业运等主题，形成适合阅读和检索的内容。"],
        ["咨询体验设计", "帮助用户在咨询前后更清晰地理解自己的问题。"],
        ["数据化研究", "积累命理术语与解读模式，建立更一致的分析标准。"]
      ],
      proofTitle: "传统与技术之间的平衡",
      proofCopy: "四柱天命研究所重视有语境的解读，而非夸张的预言。我们把古老的出生信息转译为有助于选择与自我理解的语言。",
      faqTitle: "常见问题"
    },
    faqs: [
      ["四柱天命研究所是什么机构？", "我们是研究传统四柱命理，并将其连接到咨询与内容的专业研究所。"],
      ["可以在线咨询或联系吗？", "可以。请通过 contact@sajucm.com 或 +82-070-8095-7405 联系我们。"],
      ["sajucmlab.com 是什么网站？", "这是介绍 SajuCM 研究、内容和数据化命理洞察的落地页。"]
    ]
  },
  en: {
    lang: "en",
    path: "/en/",
    locale: "en_US",
    label: "English",
    title: "SajuCM Lab | Saju Research and Consultation Insights",
    description: "SajuCM Lab connects traditional Four Pillars interpretation with research, content, data, and consultation experience.",
    eyebrow: "SajuCM Lab",
    heroTitle: "We make the language of Saju clearer, steadier, and more useful.",
    heroCopy: "SajuCM Lab turns traditional Four Pillars knowledge into structured content, research data, and consultation flows that help people understand their questions with more context.",
    primaryCta: "Contact us",
    secondaryCta: "Company site",
    blogLabel: "Blog",
    nav: ["Research", "Services", "FAQ", "Contact"],
    stats: [
      ["Saju content", "Search-friendly interpretation resources"],
      ["Consulting insight", "Question-led reading frameworks"],
      ["Knowledge data", "Repeatable research structure"]
    ],
    sections: {
      researchTitle: "Research-led Saju",
      researchCopy: "We structure traditional concepts for modern readers and refine our content and analysis around recurring questions from real consultation contexts.",
      servicesTitle: "What we build",
      services: [
        ["Four Pillars content", "We publish practical resources on fortune cycles, compatibility, aptitude, and business luck."],
        ["Consultation UX", "We design clearer before-and-after flows so users can understand their own questions better."],
        ["Data-informed research", "We organize terminology and interpretation patterns into a more consistent knowledge base."]
      ],
      proofTitle: "Between tradition and technology",
      proofCopy: "SajuCM Lab favors contextual interpretation over exaggerated prediction. We translate an old input system into language that supports self-understanding and better choices.",
      faqTitle: "FAQ"
    },
    faqs: [
      ["What is SajuCM Lab?", "SajuCM Lab is a research studio for traditional Four Pillars knowledge, consultation, and content."],
      ["Can I contact you online?", "Yes. Email contact@sajucm.com or call +82-070-8095-7405."],
      ["What is sajucmlab.com?", "It is a landing site for SajuCM research, content, and data-informed Saju insights."]
    ]
  }
};

function schemaFor(page) {
  const url = `${siteUrl}${page.path}`;
  const orgId = `${siteUrl}/#organization`;
  const localBusinessId = `${siteUrl}/#localbusiness`;
  const personId = `${siteUrl}/#person`;
  const articleId = `${url}#article`;

  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": orgId,
        "name": business.koName,
        "alternateName": [business.hanjaName, "SajuCM Lab"],
        "url": siteUrl,
        "sameAs": [companyUrl],
        "email": business.email,
        "telephone": business.telephone,
        "taxID": business.businessNumber,
        "contactPoint": {
          "@type": "ContactPoint",
          "telephone": business.telephone,
          "email": business.email,
          "contactType": "customer support",
          "availableLanguage": ["Korean", "Japanese", "Chinese", "English"]
        },
        "address": {
          "@type": "PostalAddress",
          "streetAddress": business.address.street,
          "addressLocality": business.address.locality,
          "addressRegion": business.address.region,
          "addressCountry": business.address.country
        }
      },
      {
        "@type": "LocalBusiness",
        "@id": localBusinessId,
        "name": business.koName,
        "alternateName": business.hanjaName,
        "url": siteUrl,
        "email": business.email,
        "telephone": business.telephone,
        "priceRange": "$$",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": business.address.street,
          "addressLocality": business.address.locality,
          "addressRegion": business.address.region,
          "addressCountry": business.address.country
        },
        "parentOrganization": { "@id": orgId }
      },
      {
        "@type": "Person",
        "@id": personId,
        "name": "김영준",
        "alternateName": `${business.koName} 대표 김영준`,
        "jobTitle": "사주천명연구소 대표",
        "worksFor": { "@id": orgId },
        "knowsAbout": ["Four Pillars of Destiny", "Saju", "명리학", "사주명리", "운세 상담"]
      },
      {
        "@type": "Article",
        "@id": articleId,
        "headline": page.title,
        "description": page.description,
        "inLanguage": page.lang,
        "url": url,
        "author": { "@id": personId },
        "publisher": { "@id": orgId },
        "datePublished": "2026-06-19",
        "dateModified": "2026-06-19",
        "mainEntityOfPage": url
      },
      {
        "@type": "FAQPage",
        "@id": `${url}#faq`,
        "inLanguage": page.lang,
        "mainEntity": page.faqs.map(([question, answer]) => ({
          "@type": "Question",
          "name": question,
          "acceptedAnswer": {
            "@type": "Answer",
            "text": answer
          }
        }))
      }
    ]
  };
}

Object.values(locales).forEach((page) => {
  page.business = business;
  page.companyUrl = companyUrl;
  page.siteUrl = siteUrl;
  page.schema = schemaFor(page);
});

module.exports = locales;
