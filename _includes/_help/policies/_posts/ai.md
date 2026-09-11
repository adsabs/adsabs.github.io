This policy outlines the principles, scope, and practices guiding the use of Artificial Intelligence (AI) and Machine Learning (ML) within the Astrophysics Data System (ADS) and Science Explorer (SciX). It defines our ethical framework, provides clarity on terminology and usage contexts, and establishes boundaries between research and operational applications.

## Guiding principles behind AI/ML at ADS/SciX
**Accuracy**: we will ensure that the information provided is accurate and reliable. Technologies that produce spurious results will not be used.

**Privacy**: we will protect private personal information and prevent the harvesting of identifying details, such as email addresses, from the indexed information.

**Respect**: we will comply with agreements with publishers and strictly follow copyright laws. ADS/SciX will monitor usage to prevent third parties from circumventing these agreements.

**Responsible use**: we will follow the Smithsonian Institution’s policies on responsible use of AI.

### Definitions
Artificial intelligence and machine learning are often used interchangeably, but in reality are slightly different:
 
**Machine Learning (ML)**: A subset of AI focused on algorithms that learn patterns from data and improve over time without explicit reprogramming. Examples: small language models, text classification, entity recognition, citation prediction.

**Artificial Intelligence (AI)**: A broader field encompassing systems designed to perform tasks that typically require human intelligence, such as reasoning, summarization, or dialogue. Examples: large language models, generative AI systems.

## Where We Use AI and ML

Our ultimate goal with our AI/ML efforts is to benefit ADS/SciX users and to advance the reach and pace of scientific discovery. We also generally follow the principles of open science and aim to make all of our models, datasets, and pipelines open and permissive to re-use. These efforts also benefit ADS/SciX operations by improving efficiency, data quality, and scalability. Our AI/ML work spans three different arenas:

**ADS/SciX-created machine learning datasets and small language models**
  - Expert curated, publicly available, permissively licensed  
  - Datasets and models are hosted on [Hugging Face](https://huggingface.co/adsabs) 
  - Examples: 
    - Training and evaluating models on curated, labeled datasets to recognize patterns, classify content, and improve predictive accuracy 
    - Fine-tuning or otherwise adapting LLMs for experimentation and domain-specific tasks, while ensuring transparency and reproducibility

**Data enrichment with AI/ML pipelines**
  - Enhancing metadata quality and scientific discoverability, using AI and ML techniques  
  - Examples: 
    - Automating extraction of structured information (e.g., entities, relationships, keyword/topic classifications) from unstructured sources to improve metadata quality 
    - Use of conditional random fields to convert plain-text reference strings into structured metadata to match to existing records 
    - Applying reasoning and generative techniques to infer missing context, connect related research objects, and augment tagging of metadata 

**Information retrieval features and capabilities with large language models**
  - Experimenting with a new way of searching and synthesizing information
  - Examples:
    - Leveraging learned representations to improve ranking, clustering, relevance scoring, and similarity search within search, discovery, and recommendation systems
    - Enabling natural-language queries and summarization tools that help users explore and contextualize scientific information in new ways
    - Exploring retrieval-augmented generation (RAG) systems that can answer user questions, synthesize information across multiple sources, and provide citations to the underlying literature.

Note that some of these use cases are currently publicly available or in production, while others are still in development.

## Data Stewardship
Our corpus of over 30 million metadata records and 14M full-text documents is assembled in concordance with publishers and is subject to our legal agreements with those publishers. Therefore, we need to adhere to the terms of use and licensing agreed upon in negotiations with publishers, which affect the use of this content to train models and as input to generative AI.

ADS/SciX is actively working to capture and expose licensing metadata for scholarly content. This will allow users and downstream systems to distinguish between content that is openly licensed (e.g., CC&#8209;BY) and content that remains subject to publisher restrictions. Improving the visibility of licensing information will support responsible reuse of scientific literature, including AI and machine learning applications, while ensuring compliance with applicable terms of use.

To ensure compliance with these guidelines and agreements, ADS/SciX applies the following steps as part of its data governance policies:
  - Full-text content is not shared with the public but is used internally to support indexing and discovery.
  - We do not use licensed publisher content to train systems intended to generate substitute versions of scholarly articles or other text that could reasonably replace the original work.
  - Licensed content is tagged by journal and publisher and strictly isolated in downstream processes.
  - Upon termination of a content license, relevant data is removed from ADS/SciX indices and models in accordance with agreements.
  - No user-generated content or Personally Identifiable Information (PII) is used for training or inference.
