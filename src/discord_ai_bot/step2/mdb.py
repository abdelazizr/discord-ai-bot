from replit import db

# URLs and their corresponding custom keys
urls = {
    "deep-dive-into-rag-with-langchain": "https://dev.ubuntuhive.tech/en-us/articles/deep-dive-into-rag-with-langchain/",
    "exploring-new-chatgpt-features": "https://dev.ubuntuhive.tech/en-us/articles/exploring-new-chatgpt-features-/",
    "build-small-apps-with-llms": "https://dev.ubuntuhive.tech/en-us/articles/build-small-apps-with-llms/",
    "docker-orchestra-swarm-k8s-kubernetes-for-beginners": "https://dev.ubuntuhive.tech/en-us/articles/docker-orchestra-swarm-k8s-kubernetes-for-beginners/",
    "devops-from-scratch-automated-basics": "https://dev.ubuntuhive.tech/en-us/articles/devops-from-scratch-automated-basics/",
    "from-networks-to-http-and-apis": "https://dev.ubuntuhive.tech/en-us/articles/from-networks-to-http-and-apis/",
    "data-and-cloud-infrastructure-as-code": "https://dev.ubuntuhive.tech/en-us/articles/data-and-cloud-infrastructure-as-code/"
}

# Store in the database under the 'articles' key
db["articles"] = urls

