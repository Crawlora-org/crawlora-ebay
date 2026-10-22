use crawlora_ebay::{Client, EbaySellerParams, ModelEbaySellerResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .ebay
        .seller(EbaySellerParams {
            seller: Some("musicmagpie".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelEbaySellerResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
