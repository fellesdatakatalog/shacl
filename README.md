# shacl

Playground for shacl-based hackathon ideas

## Intended workflow:
- Clone this repository
- Create a new branch, with a suitable name. Maybe the name of your team?
- Start coding!                               

## What language should I use?
- Any language is fine, as long as you can create a Dockerfile for it
- You'll likely get the most help from our developers if you stick to Java/Kotlin, Node/Next.js, Python, Go or Rust

## Where do I put my code?
Your code can be placed in the root folder.  
See for example [fdk-statistics-service](https://github.com/Informasjonsforvaltning/fdk-statistics-service)
```
hackathon-autoharvest/
├── .github
│   └── workflows
├── deploy
│   ├── base
│   │   ├── deployment.yaml
│   │   ├── kustomization.yaml
│   │   └── service.yaml
│   └── hackathon
│       ├── env.yaml
│       ├── ingress.yaml
│       └── kustomization.yaml
├── Dockerfile
└── src
```

## How to deploy my app?
- Fix all TODOS in the kustomize setup/workflows
- Make sure you have a working Dockerfile
- Push to branch
- That's it! Your code will be deployed automatically

## How do I access my app?
- Your app will be available at an autogenerated IP address, which you can find in the GitHub Actions log
- Or ask in [slack](https://offentlig-paas-no.slack.com/archives/C07PUV96YKV)

## Something went wrong!
- Check the logs in the GitHub Actions tab
- Ask for help in [slack](https://offentlig-paas-no.slack.com/archives/C07PUV96YKV)
- (If you have been granted access to GCP/k8s, you can also check the application logs via kubectl or in the Google Cloud Console)

## How about some environment variables?
- Add them to deploy/hackathon/env.yaml, as per the included example

## Secrets?
If you have been granted access to GCP/k8s, go ahead and create a new secret via kubectl:

```kubectl create secret generic <secret-name> --from-literal=<key>=<value>```
- Refer to your own secret in deploy/hackathon/env.yaml

If you don't have access:
- Create a new issue in this repository, tag it with the "secret" label
- Describe what you need, (i.e. secret name, expected keys)
- Someone will be in touch shortly, if necessary
- Uncomment L16-18 in deploy/hackathon/env.yaml
- Refer to env vars in your code as usual
- A secret should now be available in your app as an environment variable after deployment

## What if I have multiple apps?
If you want to deploy multiple apps, place each app in its individual subfolder.  
You will need to do the same with the deploy-folders, and copy the Kustomization files into each app-folder.
You will also need to modify L20 & L36 in .github/workflows/deploy.yaml  
Also, L6 in deploy/hackathon/<app-name>/kustomization.yaml must be updated to "../../base/<app-name>"
See for example [catalog-frontend](https://github.com/Informasjonsforvaltning/catalog-frontend) or [this test branch](https://github.com/fellesdatakatalog/hackathon-autoharvest/tree/test)
```
hackathon-autoharvest/
├── .github
│   └── workflows
├── app1
│   ├── Dockerfile
│   └── src
├── app2
│   ├── Dockerfile
│   └── src
└── deploy
    ├── base
    │   ├── app1
    │   └── app2
    └── hackathon
        ├── app1
        └── app2
```